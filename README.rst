==================================
IOS&Andorid API and Django Rest Framework
==================================

--------
Overview
--------

**App API support for Django REST Framework**

* Documentation: None
* Format specification: http://jsonapi.org/format/


By default, Django REST Framework will produce a request like::

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
    $ django-admin migrate --settings=example.settings
    $ django-admin loaddata drf_example --settings=example.settings
    $ django-admin runserver --settings=example.settings

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


``rest_framework_app_api`` assumes you are using class-based views in Django
Rest Framework.


Settings
^^^^^^^^

::

    REST_FRAMEWORK = {
        'PAGE_SIZE': 10,

        # rest_framework_json_api
        'EXCEPTION_HANDLER': 'rest_framework_app_api.exceptions.exception_handler',
        'DEFAULT_PAGINATION_CLASS': 'rest_framework_app_api.pagination.JsonApiPageNumberPagination',
    }



