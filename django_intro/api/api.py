from rest_framework import routers

from . import viewsets

posts_router = routers.DefaultRouter()
posts_router.register(r"posts", viewsets.PostsViewSet, basename="post")


users_router = routers.DefaultRouter()
users_router.register(r"users", viewsets.UserViewSet, basename="user")