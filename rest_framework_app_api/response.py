from rest_framework import status
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from django.utils import six
from .settings import app_api_settings
from .utils import api_dic_response, api_dic_list


class APIResponse(Response):
    """
    An HttpResponse that allows its data to be rendered into
    arbitrary media types.
    """

    def __init__(self, data=None, code=None, msg=None,
                 status=status.HTTP_200_OK,
                 template_name=None, headers=None,
                 exception=False, content_type=None):
        data_dic = api_dic_response(data=data, code=code, msg=msg)
        super(APIResponse, self).__init__(data=data_dic, status=status, template_name=template_name, headers=headers, exception=exception, content_type=content_type)

    def data_update_value(self, kwargs):
        if kwargs and isinstance(kwargs, dict) and kwargs.keys():
            self.data.update(kwargs)


def response_app_success(data=None, msg=None):
    """
    :return simple success response
    """
    return APIResponse(data=data, code=app_api_settings.DEFAULT_APP_CODE_SUCCESS, msg=msg, status=status.HTTP_200_OK)


def response_app_error(data=None, code=app_api_settings.DEFAULT_APP_CODE_FAIL, msg=app_api_settings.DEFAULT_APP_MSG_UNNONE):
    """
    :return simple error response
    """
    return APIResponse(data=data, code=code, msg=msg, status=status.HTTP_200_OK)


def response_app_list(list_data=None, total_count=0, total_pages=0, kwargs=None):
    json_dict = api_dic_list(list_data=list_data, total_count=total_count, total_pages=total_pages, kwargs=kwargs)
    return response_app_success(data=json_dict)