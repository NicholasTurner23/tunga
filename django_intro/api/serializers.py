from blog_post.models import (
    Posts
    )
from blog_user.models import (
    User
    )
from rest_framework import serializers


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Posts
        fields = ("id", "title", "body", "author")


class UserSerializer(serializers.HyperlinkedModelSerializer):
    posts = PostSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = ("id", "email", "first_name", "last_name", "phone_number", "posts")

        depth = 1