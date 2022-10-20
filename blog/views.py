from django.shortcuts import render, reverse
from .models import BlogPost
from .forms import BlogForm
from django.contrib import messages

# Create your views here.
def view_blog(request):
    """ A view to show all products """

    posts = BlogPost.objects.all()

    context = {
        'posts': posts,
    }
    
    return render(request, 'blog/blog.html', context)


def create_post(request):
    """ View to create a blog post """
    if request.method == 'POST':
        form_data = {
            'blog_title': request.POST['blog_title'],
            'author': request.POST['author'],
            'content': request.POST['content'],
        }

        blog_form = BlogForm(form_data)
        if blog_form.is_valid():
            blog_form.save()
        else:
            messages.error(request, 'There was an error with the form. Please try again.')
    else:
        blog_form = BlogForm()
    
    template = 'blog/create_post.html'
    context = {
        'blog_form': blog_form,
    }

    return render(request, template, context)