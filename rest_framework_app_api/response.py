from rest_framework import status
from rest_framework.response import Response
from .settings import app_api_settings
from .utils import api_dic_response, api_dic_list, api_dic_limit_list


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
        super(APIResponse, self).__init__(data=data_dic, status=status, template_name=template_name, headers=headers,
                                          exception=exception, content_type=content_type)

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
    """
    :return page list response
    """
    json_dict = api_dic_list(list_data=list_data, total_count=total_count, total_pages=total_pages, kwargs=kwargs)
    return response_app_success(data=json_dict, msg=app_api_settings.DEFAULT_APP_MSG_SEARCH_SUCCESS)


def response_app_list_limit(list_data=None, limit=0, offset=0, kwargs=None):
    """
    :return limit list response
    """
    json_dict = api_dic_limit_list(list_data=list_data, limit=limit, offset=offset, kwargs=kwargs)
    return response_app_success(data=json_dict, msg=app_api_settings.DEFAULT_APP_MSG_SEARCH_SUCCESS)


def response_app_error_params(message='参数错误', data=None):
    return response_app_error(code=status.HTTP_400_BAD_REQUEST, msg=message, data=data)


def response_app_error_unauth(message='未登录 或者token过期', data=None):
    return response_app_error(code=status.HTTP_401_UNAUTHORIZED, msg=message, data=data)


def response_app_error_forbidden(message='您没有该操作权限', data=None):
    return response_app_error(code=status.HTTP_403_FORBIDDEN, msg=message, data=data)


def response_app_error_method(message='方法错误', data=None):
    return response_app_error(code=status.HTTP_405_METHOD_NOT_ALLOWED, msg=message, data=data)


def response_app_error_server(message='服务器错误', data=None):
    return response_app_error(code=status.HTTP_500_INTERNAL_SERVER_ERROR, msg=message, data=data)