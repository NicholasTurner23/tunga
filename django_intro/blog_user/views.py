from django.contrib.auth.mixins import LoginRequiredMixin
from django_tables2.views import SingleTableMixin
from django_filters.views import FilterView
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from . import filters, tables, models
from blog_post.models import Posts


class UserList(LoginRequiredMixin, SingleTableMixin, FilterView, ListView):
    model = models.User
    table_class = tables.UserTable
    filterset_class = filters.UserFilter
    paginate_by = 50


class DetailUser(DetailView):
    model = models.User
    success_url = reverse_lazy("blog_user:users")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        author_id = self.kwargs["pk"]
        author = self.request.user
        if author_id != author.id:
            author = models.User.objects.filter(id=author_id).first()
        
        if author:
            posts = Posts.objects.filter(author=author)
        context['posts'] = posts
        return context

