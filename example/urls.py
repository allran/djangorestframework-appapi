from django.conf import settings
from django.conf.urls import include, url
from rest_framework import routers

from example.views import (
    AuthorViewSet,
    BlogViewSet,
)

router = routers.DefaultRouter(trailing_slash=False)

router.register(r'blogs', BlogViewSet)
router.register(r'authors', AuthorViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'entries/(?P<entry_pk>[^/.]+)/blog$',
        BlogViewSet.as_view({'get': 'retrieve'}),
        name='entry-blog'),
    url(r'entries/(?P<entry_pk>[^/.]+)/authors$',
        AuthorViewSet.as_view({'get': 'list'}),
        name='entry-authors'),
    url(r'^authors/(?P<pk>[^/.]+)/(?P<related_field>\w+)/$',
        AuthorViewSet.as_view({'get': 'retrieve_related'}),
        name='author-related'),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
