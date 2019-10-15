from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from rest_framework.utils.urls import remove_query_param, replace_query_param
from .response import response_app_list, response_app_list_limit


class AppApiPageNumberPagination(PageNumberPagination):
    """
    A app-api compatible pagination format.
    """
    def build_link(self, index):
        if not index:
            return None
        url = self.request and self.request.build_absolute_uri() or ''
        return replace_query_param(url, self.page_query_param, index)

    def get_paginated_response(self, data):
        response = response_app_list(list_data=data, total_count=self.page.paginator.count,
                                     total_pages=self.page.paginator.num_pages)
        return response


class AppApiLimitOffsetPagination(LimitOffsetPagination):
    """
    A limit/offset based style. For example:

    .. code::

        http://api.example.org/accounts/?limit=100
        http://api.example.org/accounts/?offset=400&limit=100

    """
    def get_last_link(self):
        if self.count == 0:
            return None

        url = self.request.build_absolute_uri()
        url = replace_query_param(url, self.limit_query_param, self.limit)
        offset = (self.count // self.limit) * self.limit

        if offset <= 0:
            return remove_query_param(url, self.offset_query_param)

        return replace_query_param(url, self.offset_query_param, offset)

    def get_first_link(self):
        if self.count == 0:
            return None

        url = self.request.build_absolute_uri()
        return remove_query_param(url, self.offset_query_param)

    def get_paginated_response(self, data):
        response = response_app_list_limit(list_data=data, limit=self.count, offset=self.offset)
        return response
