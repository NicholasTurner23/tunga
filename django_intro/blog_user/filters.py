import django_filters
from . import models


class UserFilter(django_filters.FilterSet):
    first_name = django_filters.CharFilter(
        lookup_expr="icontains", label="first name"
    )
    last_name = django_filters.CharFilter(lookup_expr="icontains", label="last name")

    class Meta:
        model = models.User
        fields = ["first_name", "last_name"]
