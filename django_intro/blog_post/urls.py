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
    path("create", CreateBlogPost.as_view(), name="create-post"),
    path("update/<int:pk>", UpdateBlogPost.as_view(), name="update-post"),
    path("<int:pk>", DetailBlogPost.as_view(), name="post-details"),
    path("delete/<int:pk>", DeleteBlogPost.as_view(), name="delete-post")
]