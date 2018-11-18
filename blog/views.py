from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView, CreateView

from .models import Blog


# 記事一覧画面
class BlogListView(ListView):
    model = Blog


# 記事詳細画面
class BlogDetailView(DetailView):
    model = Blog


# 記事投稿画面
class BlogCreateView(CreateView):
    model = Blog
    fields = ['content']
    success_url = reverse_lazy('index')  # トップページへ遷移
