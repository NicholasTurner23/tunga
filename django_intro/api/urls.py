from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .api import (
    posts_router,
    users_router
)
from .views import login

router = DefaultRouter()
router.registry.extend(posts_router.registry)
router.registry.extend(users_router.registry)

urlpatterns = [
    path(r"", include(router.urls)),
    path(r"auth/login/", login),
]