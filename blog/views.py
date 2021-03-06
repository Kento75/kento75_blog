from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy
from django.contrib import messages

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Blog

from .froms import BlogForm


# 記事一覧画面
class BlogListView(ListView):
    model = Blog
    context_object_name = 'blogs'
    paginate_by = 5  # 5件毎にページネーション


# 記事詳細画面
class BlogDetailView(DetailView):
    model = Blog
    context_object_name = 'blog'


# 記事投稿画面
class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    form_class = BlogForm
    success_url = reverse_lazy('index')  # トップページへ遷移
    login_url = '/login'
    template_name = 'blog/blog_create_form.html'

    def form_valid(self, form):
        messages.success(self.request, '保存しました')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, '保存に失敗しました')
        return super().form_invalid(form)


# 記事編集画面
class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Blog
    form_class = BlogForm
    login_url = '/login'
    template_name = 'blog/blog_update_form.html'

    def get_success_url(self):
        blog_pk = self.kwargs['pk']  # 記事IDを取得
        url = reverse_lazy('detail', kwargs={'pk': blog_pk})
        return url  # 記事詳細画面へ遷移

    def form_valid(self, form):
        messages.success(self.request, '更新されました')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, '更新に失敗しました')
        return super().form_invalid(form)


# 記事削除画面
class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Blog
    success_url = reverse_lazy('index')  # トップページへ遷移
    login_url = '/login'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, '削除しました')
        return super().delete(request, *args, **kwargs)
