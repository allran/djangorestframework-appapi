from rest_framework import routers

from blog.views import BlogViewSet, AuthorViewSet, UserFavViewset

api_django_router = routers.SimpleRouter()
api_django_router.register(r'blog', BlogViewSet, base_name='blog')
api_django_router.register(r'author', AuthorViewSet, base_name='author')
api_django_router.register(r'userfavs', UserFavViewset, base_name="userfavs")  # 配置用户收藏的url
