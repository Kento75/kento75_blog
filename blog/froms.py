from django import forms

from .models import Blog


class BlogForm(forms.ModelForm):
    # タイトル
    title = forms.CharField(widget=forms.TextInput(attrs={'size': 50}))
    # テキストボックス
    content = forms.CharField(widget=forms.TextInput(attrs={'size': 4000}))

    class Meta:
        model = Blog
        fields = ['title', 'content']
