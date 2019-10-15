from rest_framework.views import exception_handler as drf_exception_handler
from .response import APIResponse
from rest_framework import status
from .settings import app_api_settings


def exception_handler(exc, context):
    """
    Returns the response that should be used for any given exception.

    By default we handle the response.py `APIException`.
    """
    response = drf_exception_handler(exc, context)
    if not response:
        return APIResponse(code=app_api_settings.DEFAULT_APP_CODE_FAIL, msg=app_api_settings.DEFAULT_APP_MSG_UNNONE, status=status.HTTP_200_OK)
    message = str(response.data)
    return APIResponse(code=response.status_code, msg=message, status=status.HTTP_200_OK)
