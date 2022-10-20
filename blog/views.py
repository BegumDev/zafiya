from django.shortcuts import render
from .models import BlogPost

# Create your views here.
def view_blog(request):
    """ A view to show all products """

    posts = BlogPost.objects.all()

    context = {
        'posts': posts,
    }
    
    return render(request, 'blog/blog.html', context)