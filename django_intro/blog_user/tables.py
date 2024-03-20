import django_tables2 as tables
from . import models

class UserTable(tables.Table):
    id = tables.LinkColumn()

    class Meta:
        model = models.User
        fields = [
            "email",
            "first_name",
            "last_name",
            "phone_number",
        ]
        template_name = "django_tables2/bootstrap-responsive.html"