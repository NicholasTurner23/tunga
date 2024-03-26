from . import serializers
from rest_framework import viewsets
from blog_post.models import Posts
from blog_user.models import User


class PostsViewSet(viewsets.ModelViewSet):
    queryset = Posts.objects.all().order_by("-created")
    serializer_class = serializers.PostSerializer
    filter_fields = ("title",)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by("-created")
    serializer_class = serializers.UserSerializer
    filter_fields = ("first_name",)