IOS&Andorid API and Django Rest Framework

--------
Overview
--------

**App API support for Django REST Framework**

* Documentation: None
* Format specification: http://jsonapi.org/format/


1. By default, Django REST Framework will produce a request like::

    http://example.com/api/1.0/identities/?page=1

and then the response like::

    {
        "count": 200,
        "msg": "success!",
        "data": {
            "list": [
                {
                    "id": 3,
                    "username": "john1",
                    "full_name": "John Coltrane1"
                },
                 {
                    "id": 4,
                    "username": "john2",
                    "full_name": "John Coltrane2"
                },
            ],
            "total_count": 2,
            "total_pages": 1
        }
    }

2. if you want get object info, you will produce a request like:
    http://example.com/api/1.0/identities/1/

and then the response like:

::

    {
        "count": 200,
        "msg": "success!",
        "data": {
            "id": 1,
            "username": "john2",
            "full_name": "John Coltrane2"
        }
    }


-----
Goals
-----

As a Django REST Framework APP API (short DJA) we are trying to address following goals:

1. Support the `REST_FRAMEWORK_APPAPI` to compliance

2. Be as compatible with `Django REST Framework`_ as possible

3. Have sane defaults to be as easy to pick up as possible

4. Be solid and tested with good coverage

5. Be performant

.. _JSON API: http://jsonapi.org
.. _Django REST Framework: https://www.django-rest-framework.org/

------------
Requirements
------------

1. Python (3.5, 3.6, 3.7)
2. Django (1.11, 2.1, 2.2)
3. Django REST Framework (3.10)

We **highly** recommend and only officially support the latest patch release of each Python, Django and REST Framework series.

------------
Installation
------------

From PyPI
^^^^^^^^^

::

    $ pip install djangorestframework-appapi

From Source
^^^^^^^^^^^

::

    $ git clone https://github.com/allran/djangorestframework-appapi.git
    $ cd django-rest-framework-app-api
    $ pip install -e .


Running the example app
^^^^^^^^^^^^^^^^^^^^^^^

It is recommended to create a virtualenv for testing. Assuming it is already
installed and activated:

::

    $ git clone https://github.com/allran/djangorestframework-appapi.git
    $ cd django-rest-framework-app-api
    $ pip install -U -e . -r requirements.txt
    $ django-admin migrate --settings=example_project.settings
    $ django-admin loaddata drf_example --settings=example_project.settings
    $ django-admin runserver --settings=example_project.settings

Browse to http://localhost:8000


Running Tests and linting
^^^^^^^^^^^^^^^^^^^^^^^^^

It is recommended to create a virtualenv for testing. Assuming it is already
installed and activated:

::

    $ pip install -Ur requirements.txt
    $ flake8
    $ pytest

-----
Usage
-----

一. ``rest_framework_app_api`` assumes you are using class-based renderers in Django
Rest Framework.

::

    REST_FRAMEWORK = {
        'DEFAULT_RENDERER_CLASSES': (
            'rest_framework_app_api.renderers.JSONRenderer',
        ),
    }

then you can get the app response data

::

    {
        "data": [
            {
                "id": 1,
                "name": "张三"
            },
            {
                "id": 2,
                "name": "李四"
            }
        ],
        "code": 200,
        "msg": "OK"
    }


二. ``rest_framework_app_api`` assumes you are using class-based views in Django
Rest Framework.

if you use like ListAPIView in ``from rest_framework.generics import ListAPIView``, please replace with ``from rest_framework_app_api.generics import ListAPIView``.

::

    from snippets.models import Snippet
    from snippets.serializers import SnippetSerializer
    from rest_framework_app_api import generics

    class SnippetList(generics.ListCreateAPIView):
        queryset = Snippet.objects.all()
        serializer_class = SnippetSerializer

    class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
        queryset = Snippet.objects.all()
        serializer_class = SnippetSerializer


1. if you use like ListModelMixin in ``from rest_framework.mixins import ListModelMixin``, please replace with ``from rest_framework_app_api.mixins import ListModelMixin``.

::

    from snippets.models import Snippet
    from snippets.serializers import SnippetSerializer
    from rest_framework_app_api import mixins
    from rest_framework import generics

    class SnippetDetail(mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        generics.GenericAPIView):
        queryset = Snippet.objects.all()
        serializer_class = SnippetSerializer

        def get(self, request, *args, **kwargs):
            return self.retrieve(request, *args, **kwargs)

        def put(self, request, *args, **kwargs):
            return self.update(request, *args, **kwargs)

        def delete(self, request, *args, **kwargs):
            return self.destroy(request, *args, **kwargs)

2. if you use like APIView in ``from rest_framework.views import APIView``, please replace with ``from rest_framework_app_api.views import APIView``.

::

    from snippets.models import Snippet
    from snippets.serializers import SnippetSerializer
    from rest_framework_app_api.views import APIView
    from rest_framework_app_api.response import APIResponse
    from rest_framework import status

    class SnippetList(APIView):
        """
        List all snippets, or create a new snippet.
        """
        def get(self, request, format=None):
            snippets = Snippet.objects.all()
            serializer = SnippetSerializer(snippets, many=True)
            return APIResponse(serializer.data)

        def post(self, request, format=None):
            serializer = SnippetSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return APIResponse(serializer.data)
            return APIResponse(serializer.errors)

    class SnippetDetail(APIView):
        """
        Retrieve, update or delete a snippet instance.
        """
        def get(self, request, pk, format=None):
            snippet = self.get_object(pk)
            serializer = SnippetSerializer(snippet)
            return APIResponse(serializer.data)

        def put(self, request, pk, format=None):
            snippet = self.get_object(pk)
            serializer = SnippetSerializer(snippet, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return APIResponse(serializer.data)
            return APIResponse(serializer.errors, code=status.HTTP_400_BAD_REQUEST)

        def delete(self, request, pk, format=None):
            snippet = self.get_object(pk)
            snippet.delete()
            return APIResponse(code=status.HTTP_204_NO_CONTENT)

3. if you use like ModelViewSet in ``from rest_framework.viewsets import ModelViewSet``, please replace with ``from rest_framework_app_api.viewsets import ModelViewSet``.

::

    from snippets.models import Snippet
    from rest_framework_app_api import viewsets

    class SnippetViewSet(viewsets.ModelViewSet):
        queryset = Author.objects.all()
        serializer_class = AuthorSerializer

4. if you use like Response in ``from rest_framework.response import Response``, please replace with ``from rest_framework_app_api.response import APIResponse``.


Settings
^^^^^^^^

rest_framework setting

::

    REST_FRAMEWORK = {
        'PAGE_SIZE': 10,

        # rest_framework custom setting
        'EXCEPTION_HANDLER': 'rest_framework_app_api.exceptions.exception_handler',
        'DEFAULT_PAGINATION_CLASS': 'rest_framework_app_api.pagination.AppApiPageNumberPagination',
    }

rest_framework_app_api setting

::

    REST_FRAMEWORK_APPAPI = {
        # rest_framework_app_api code
        'DEFAULT_APP_CODE_SUCCESS': 200,  # default success code
        'DEFAULT_APP_CODE_FAIL': 0,  # default error code

        # rest_framework_app_api msg
        'DEFAULT_APP_MSG_CREAT_SUCCESS': 'create success！',
        'DEFAULT_APP_MSG_UPDATE_SUCCESS': 'update success！',
        'DEFAULT_APP_MSG_DELETE_SUCCESS': 'delete success！',
        'DEFAULT_APP_MSG_SEARCH_SUCCESS': 'get data success！',
        'DEFAULT_APP_MSG_SEARCH_NODATA': 'no data！',
        'DEFAULT_APP_MSG_UNNONE': 'unknown error！',
    }

