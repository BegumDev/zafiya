from django import forms
from .models import BlogPost, PostComment


class BlogForm(forms.ModelForm):
    """ Blog Form """
    class Meta:
        model = BlogPost
        fields = ['blog_title', 'content']


class CommentForm(forms.ModelForm):
    """ Comment Form """
    class Meta:
        model = PostComment
        fields = ['comment']
