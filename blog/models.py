from django.db import models
from django.contrib.auth.models import User


class BlogPost(models.Model):
    blog_title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    created_on = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return self.blog_title


class PostComment(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE,
                             related_name='comments')
    comment_author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(null=False)
    date = models.DateTimeField(auto_now_add=True)
    