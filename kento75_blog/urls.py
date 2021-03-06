"""kento75_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.contrib.auth.views import LoginView, LogoutView

from blog.views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView


urlpatterns = [
    path('', BlogListView.as_view(), name='index'),                    # 記事一覧画面
    path('<int:pk>/update', BlogUpdateView.as_view(), name='update'),  # 記事編集画面
    path('<int:pk>/delete', BlogDeleteView.as_view(), name='delete'),  # 記事削除画面
    path('<int:pk>', BlogDetailView.as_view(), name='detail'),         # 記事詳細画面
    path('create', BlogCreateView.as_view(), name='create'),           # 記事投稿画面
    path('login', LoginView.as_view(template_name='login.html'), name='login'),      # ログイン画面
    path('logout', LogoutView.as_view(template_name='logout.html'), name='logout'),  # ログアウト画面
    path('admin/', admin.site.urls),
]
