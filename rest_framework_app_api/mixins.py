"""
Basic building blocks for generic class based views.

We don't bind behaviour to http method handlers yet,
which allows mixin classes to be composed in interesting ways.
"""
from .response import APIResponse
from rest_framework import mixins as drf_mixins
from .settings import app_api_settings


class CreateModelMixin(drf_mixins.CreateModelMixin):
    """
    Create a model instance.
    """
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return APIResponse(data=serializer.data,
                           code=app_api_settings.DEFAULT_APP_CODE_SUCCESS,
                           msg=app_api_settings.DEFAULT_APP_MSG_CREAT_SUCCESS,
                           headers=headers)


class ListModelMixin(drf_mixins.ListModelMixin):
    """
    List a queryset.
    """
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return APIResponse(data=serializer.data,
                           code=app_api_settings.DEFAULT_APP_CODE_SUCCESS,
                           msg=app_api_settings.DEFAULT_APP_MSG_SEARCH_SUCCESS)


class RetrieveModelMixin(drf_mixins.RetrieveModelMixin):
    """
    Retrieve a model instance.
    """
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return APIResponse(data=serializer.data,
                           code=app_api_settings.DEFAULT_APP_CODE_SUCCESS,
                           msg=app_api_settings.DEFAULT_APP_MSG_SEARCH_SUCCESS)


class UpdateModelMixin(drf_mixins.UpdateModelMixin):
    """
    Update a model instance.
    """
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}
        return APIResponse(data=serializer.data,
                           code=app_api_settings.DEFAULT_APP_CODE_SUCCESS,
                           msg=app_api_settings.DEFAULT_APP_MSG_UPDATE_SUCCESS)


class DestroyModelMixin(drf_mixins.DestroyModelMixin):
    """
    Destroy a model instance.
    """
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return APIResponse(data={},
                           code=app_api_settings.DEFAULT_APP_CODE_SUCCESS,
                           msg=app_api_settings.DEFAULT_APP_MSG_DELETE_SUCCESS)
