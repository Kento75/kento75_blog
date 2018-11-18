from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView, CreateView, UpdateView

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


# 記事編集画面
class BlogUpdateView(UpdateView):
    model = Blog
    fields = ['content']

    def get_success_url(self):
        blog_pk = self.kwargs['pk']  # 記事IDを取得
        url = reverse_lazy('detail', kwargs={'pk': blog_pk})
        return url  # 記事詳細画面へ遷移
