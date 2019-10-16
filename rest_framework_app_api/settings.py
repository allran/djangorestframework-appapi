"""
This module provides the `app_api_settings` object that is used to access
App API REST framework settings, checking for user settings first, then falling back to
the defaults.
"""

# -*- coding: utf-8 -*-
from django.conf import settings

from rest_framework.settings import APISettings


USER_SETTINGS = getattr(settings, 'REST_FRAMEWORK_APPAPI', None)

DEFAULTS = {
    # code
    'DEFAULT_APP_CODE_SUCCESS': 200,  # 默认成功的状态值
    'DEFAULT_APP_CODE_FAIL': 0,  # 默认失败的状态值

    # msg
    'DEFAULT_APP_MSG_CREAT_SUCCESS': '创建成功！',
    'DEFAULT_APP_MSG_UPDATE_SUCCESS': '更新成功！',
    'DEFAULT_APP_MSG_DELETE_SUCCESS': '删除成功！',
    'DEFAULT_APP_MSG_SEARCH_SUCCESS': '获取成功！',
    'DEFAULT_APP_MSG_SEARCH_NODATA': '暂无数据！',
    'DEFAULT_APP_MSG_UNNONE': '未知错误！',

    # rest_framework
    # 'EXCEPTION_HANDLER': 'rest_framework_app_api.exceptions.exception_handler',
    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework_app_api.pagination.AppApiPageNumberPagination',
}

IMPORT_STRINGS = [

]


app_api_settings = APISettings(USER_SETTINGS, DEFAULTS, IMPORT_STRINGS)
