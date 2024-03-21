import logging

import requests
from apistar.exceptions import ErrorResponse
from tenacity import (
    before_sleep_log,
    retry,
    retry_if_exception,
    retry_if_exception_type,
    stop_after_attempt,
    wait_exponential,
    wait_fixed,
)

from arkindex import ArkindexClient, options_from_env

logger = logging.getLogger(__name__)

DEFAULT_CLIENT = ArkindexClient(**options_from_env())

# Time to wait before retrying the IIIF image information fetching
HTTP_GET_RETRY_BACKOFF = 10

DOWNLOAD_CHUNK_SIZE = 8192


def _is_500_error(exc):
    """
    Check if an Arkindex API error is a 50x
    This is used to retry most API calls implemented here
    """
    if not isinstance(exc, ErrorResponse):
        return False

    return 500 <= exc.status_code < 600


@retry(
    retry=retry_if_exception(_is_500_error),
    wait=wait_exponential(multiplier=2, min=3),
    reraise=True,
    stop=stop_after_attempt(5),
    before_sleep=before_sleep_log(logger, logging.INFO),
)
def retried_request(*args, **kwargs):
    """
    Proxy all Arkindex API requests with a retry mechanism
    in case of 50X errors
    The same API call will be retried 5 times, with an exponential sleep time
    going through 3, 4, 8 and 16 seconds of wait between call.
    If the 5th call still gives a 50x, the exception is re-raised
    and the caller should catch it
    Log messages are displayed before sleeping (when at least one exception occurred)
    """
    return DEFAULT_CLIENT.request(*args, **kwargs)


@retry(
    reraise=True,
    retry=retry_if_exception_type(requests.RequestException),
    stop=stop_after_attempt(3),
    wait=wait_fixed(HTTP_GET_RETRY_BACKOFF),
)
def download_file(url, path):
    """
    Download a URL into a local path, retrying if necessary
    """
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with path.open("wb") as f:
            for chunk in r.iter_content(chunk_size=DOWNLOAD_CHUNK_SIZE):
                if chunk:  # Ignore empty chunks
                    f.write(chunk)
