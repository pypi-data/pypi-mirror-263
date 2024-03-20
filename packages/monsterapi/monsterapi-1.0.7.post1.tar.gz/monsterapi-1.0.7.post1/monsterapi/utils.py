import os
import time
import logging
import requests

from functools import wraps

# Use LOGGING_LEVEL environment variable to set logging level
# Default logging level is INFO
level = os.environ.get('LOGGING_LEVEL', 'INFO')

if level == 'DEBUG':
    logging.basicConfig(level=logging.DEBUG)
elif level == 'INFO':
    logging.basicConfig(level=logging.INFO)
elif level == 'WARNING':
    logging.basicConfig(level=logging.WARNING)
elif level == 'ERROR':
    logging.basicConfig(level=logging.ERROR)
elif level == 'CRITICAL':
    logging.basicConfig(level=logging.CRITICAL)

def retry_on_status(codes={400}, retries=3, delay=5):
    """
    Decorator that retries the function when it raises a requests.HTTPError with certain status codes.

    :param codes: The HTTP status codes to retry on, default is {400}.
    :param retries: The number of retries, default is 3.
    :param delay: The delay between retries in seconds, default is 5.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(retries):
                try:
                    result = func(*args, **kwargs)
                    return result
                except requests.HTTPError as e:
                    if e.response.status_code in codes:
                        time.sleep(delay)
                    else:
                        raise e
            raise Exception("Maximum retry attempts reached, request failed.")
        return wrapper
    return decorator
