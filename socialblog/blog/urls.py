from django.urls import path
from . import views
from .models import Post, Comment
from django.views.generic import TemplateView, ListView
from django.utils import timezone

urlpatterns = [path("about/", views.AboutView.as_view(), name="about")]


class AboutView(TemplateView):
    template_name = "about.html"


class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(
            published_date__lte=timezone.now.order_by("-published_date")
        )
