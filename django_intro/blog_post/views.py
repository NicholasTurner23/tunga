from django.urls import reverse_lazy
from django.views.generic import TemplateView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib import messages
from . import forms, models
from django.views.generic.base import TemplateView



class BlogPostList(TemplateView):
    template_name = "blog_post/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        posts = models.Posts.objects.all()
        context['posts'] = posts
        return context


class CreateBlogPost(CreateView):
    model = models.Posts
    form_class = forms.PostCreateForm
    success_url = reverse_lazy("blog_post:posts")

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        try:
            self.object.save()
        except:  # noqa: E722
            messages.info(self.request, "Post has already been posted.")
            return super().form_invalid(form)
        return super().form_valid(form)
    

class UpdateBlogPost(UpdateView):
    model = models.Posts
    form_class = forms.PostCreateForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        try:
            self.object.save()
        except:  # noqa: E722
            messages.info(self.request, "A similar post exists in the system.")
            return super().form_invalid(form)
        self.object.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy("blog_post:update-post", kwargs={"pk": self.object.pk})
    

class DetailBlogPost(DetailView):
    model = models.Posts
    success_url = reverse_lazy("blog_post:posts")


class DeleteBlogPost(DeleteView):
    model = models.Posts
    success_url = reverse_lazy("blog_post:posts")

    def form_valid(self, form):
        messages.success(self.request, "The post was deleted successfully.")
        return super(DeleteBlogPost,self).form_valid(form)