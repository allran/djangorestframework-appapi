from rest_framework_app_api import viewsets
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.authentication import SessionAuthentication

from example.models import Author, Blog, UserFavorite
from example.serializers import (
    AuthorSerializer,
    BlogSerializer,
    UserFavDetailSerializer,
    UserFavSerializer
)


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class UserFavViewset(viewsets.ModelViewSet):
    """
    list:
        获取用户收藏列表
    retrieve:
        判断某个是否已经收藏
    create:
        收藏博客
    """
    # queryset = UserFav.objects.all()
    permission_classes = (IsAuthenticated, IsAuthenticatedOrReadOnly)
    serializer_class = UserFavSerializer
    lookup_field = 'blog_id'
    authentication_classes = (SessionAuthentication)

    def get_queryset(self):
        return UserFavorite.objects.filter(user=self.request.user)

    # 设置动态的Serializer
    def get_serializer_class(self):
        if self.action == "list":
            return UserFavDetailSerializer
        elif self.action == "create":
            return UserFavSerializer
        return UserFavSerializer
