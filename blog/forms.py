from django import forms
from .models import BlogPost


# class BlogForm(forms.ModelForm):
#     """ Blog Form """
#     class Meta:
#         model = BlogPost
#         fields = ('blog_title', 'author', 'content')


class BlogForm(forms.ModelForm):
    """ Blog Form """
    class Meta:
        model = BlogPost
        fields = ['blog_title', 'content']
