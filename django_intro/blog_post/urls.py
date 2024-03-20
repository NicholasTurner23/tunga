from django.urls import path
from .views import (
    BlogPostList,
    CreateBlogPost,
    UpdateBlogPost,
    DetailBlogPost,
    DeleteBlogPost
)

app_name = "blog_post"

urlpatterns = [
    path("", BlogPostList.as_view(), name="posts"),
    path("create", CreateBlogPost.as_view(), name="create-posts"),
    path("update", UpdateBlogPost.as_view(), name="update-posts"),
    path("<int:pk>", DetailBlogPost.as_view(), name="post-details"),
    path("delete/<int:pk>", DeleteBlogPost.as_view(), name="delete-post")
]