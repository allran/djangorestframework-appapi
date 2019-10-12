from datetime import datetime

from rest_framework import fields as drf_fields
from rest_framework import serializers as serializers

from example.models import (
    Author,
    Blog,
)


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'name')


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = "__all__"
