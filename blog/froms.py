from django import forms

from .models import Blog


class BlogForm(forms.ModelForm):
    # タイトル
    # テキストボックス、文字数：50
    content = forms.CharField(widget=forms.TextInput(attrs={'size': 50}))

    class Meta:
        model = Blog
        fields = ['content']
