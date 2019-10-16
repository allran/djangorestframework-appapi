"""
Provides an APIView class that is the base of all views in REST framework.
"""
from rest_framework.views import APIView as DRF_APIView
from rest_framework_app_api.response import APIResponseSuccess


class APIView(DRF_APIView):
    def options(self, request, *args, **kwargs):
        """
        Handler method for HTTP 'OPTIONS' request.
        """
        if self.metadata_class is None:
            return self.http_method_not_allowed(request, *args, **kwargs)
        data = self.metadata_class().determine_metadata(request, self)
        return APIResponseSuccess(data=data)
