from django.urls import path
from . import views
from .models import Post, Comment
from django.views.generic import TemplateView, ListView
from django.utils import timezone

urlpatterns = [path("about/", views.AboutView.as_view(), name="about")]
