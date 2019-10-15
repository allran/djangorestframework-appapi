from datetime import datetime

from rest_framework.validators import UniqueTogetherValidator
from rest_framework import serializers

from example.models import (
    Author,
    Blog,
    UserFavorite
)


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'name')


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = "__all__"


class UserFavDetailSerializer(serializers.ModelSerializer):
    # 通过blog_id拿到视频信息。就需要嵌套的Serializer
    blog = BlogSerializer()

    class Meta:
        model = UserFavorite
        fields = "__all__"


class UserFavSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = UserFavorite

        # 使用validate方式实现唯一联合
        validators = [
            UniqueTogetherValidator(
                queryset=UserFavorite.objects.all(),
                fields=('user', 'blog'),
                message="已经收藏"
            )
        ]

        fields = ("user", "video", "id")
