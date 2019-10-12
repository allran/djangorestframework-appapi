from rest_framework.pagination import PageNumberPagination
from .response import response_app_list


class JsonApiPageNumberPagination(PageNumberPagination):
    """
    列表自定义分页
    """
    def get_paginated_response(self, data):
        response = response_app_list(list_data=data, total_count=self.page.paginator.count,
                                     total_pages=self.page.paginator.num_pages)
        return response
