from .errors import (
    CustomAPIError,
    ObjectAlreadyExistError
)
from django.db import IntegrityError, DatabaseError
from rest_framework.response import Response
from sentry_sdk import capture_exception
from redis.exceptions import RedisError, ConnectionError
from drf_standardized_errors.handler import exception_handler as drf_exception_handler
from rest_framework import status


def exception_handler(exc, context=None):
    """
    Returns the response that should be used for any given exception.

    Any unhandled exceptions may return `None`, which will cause a 500 error
    to be raised.
    """
    capture_exception(exc)  # sentry catch and send actual error
    if isinstance(exc, DatabaseError):
        exc = CustomAPIError(detail="A database error occurred.", code="database_error")
    elif isinstance(exc, (RedisError, ConnectionError)):
        exc = CustomAPIError(
            detail="A redis error has occurred, this might be an issue with the redis connection",
            code="database_error",
        )

    response = drf_exception_handler(exc, context)

    if response is not None:
        # Modify the default response (optional)
        response.data["status_code"] = response.status_code

    else:
        exc = CustomAPIError(
            detail=str(exc),
            code="null",
        )
        response = drf_exception_handler(exc, context)
        response.data["status_code"] = response.status_code

    return response
