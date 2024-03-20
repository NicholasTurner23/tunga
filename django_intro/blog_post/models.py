from django.db import models
from django.db import models
from model_utils.models import TimeStampedModel
from django.urls import reverse
from blog_user.models import User


class Posts(TimeStampedModel):
    title = models.CharField(max_length=128)
    body = models.TextField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")

    def __str__(self):
        return "{} ({})".format(self.title, self.author)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ["-created"]
        unique_together = ["title", "author"]
        indexes = [
            models.Index(fields=['author'],name='author_idx'),
        ]

    def get_absolute_url(self):
        return reverse(
            "blog_post:post_details", args=[str(self.id)]
        )