from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.User)
class BlogUsers(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "email",
    )
    search_fields = [
        "first_name__last_name__email",
    ]