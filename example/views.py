from rest_framework_app_api import viewsets

from example.models import Author, Blog
from example.serializers import (
    AuthorSerializer,
    BlogSerializer,
)


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
