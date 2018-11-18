from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import DetailView

from .models import Blog


# 記事一覧画面
class BlogListView(ListView):
    model = Blog


# 記事詳細画面
class BlogDetailView(DetailView):
    model = Blog

