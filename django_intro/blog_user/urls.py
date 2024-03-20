from django.urls import path
from .views import (
    UserList,
    DetailUser
)

app_name = "blog_user"

urlpatterns = [
    path("", UserList.as_view(), name="users"),
    path("<int:pk>", DetailUser.as_view(), name="user-details"),
]