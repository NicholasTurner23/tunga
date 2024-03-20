from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.Posts)
class BlogPosts(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
    )
    search_fields = [
        "title__author",
    ]