from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Q
from .models import BlogPost, PostComment
from .forms import BlogForm, CommentForm

# Create your views here.
def view_blog(request):
    """ A view to show all products """

    posts = BlogPost.objects.all()

    # search the blog
    blog_search = None

    if request.GET:
        if 'blog_search' in request.GET:
            blog_search = request.GET['blog_search']
            if not blog_search:
                messages.error(request, "No search entered.")
                return redirect(reverse('view_blog'))
            
            queries = Q(blog_title__icontains=blog_search) | Q(content__icontains=blog_search)
            posts = posts.filter(queries)

    context = {
        'posts': posts,
        'search_for': blog_search,
    }
    return render(request, 'blog/blog.html', context)


@login_required
def create_post(request):
    """ View to create a blog post """

    form = BlogForm()

    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid:
            data = form.save(commit=False)
            data.author = User(id=request.user.id)
            data.save()

            messages.success(request, 'Blog post successfully created')
            return redirect(reverse('view_blog'))
        else:
            messages.error(request, 'There was an error with the form. Please try again.')
    else:
        form = BlogForm()
    
    template = 'blog/create_post.html'
    context = {
          'form': form,
      }

    return render(request, template, context)


def read_post(request, id):
    """ View individual post and be able to comment on them"""

    post = BlogPost.objects.get(id=int(id))

    comment_form = CommentForm()

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            instance = comment_form.save(commit=False)
            instance.post = post  # attach the comment form to the post
            instance.comment_author = request.user
            instance.save()
            messages.success(request, 'Added comment')
            return redirect(reverse('read_post', args=[post.id]))
        else:
            messages.success(request, 'Failed to add comment')
    else:
        comment_form = CommentForm()

    template = 'blog/read_post.html'
    context = {
        'post': post,
        'comment_form': comment_form,
    }
    return render(request, template, context)


def update_post(request, id):
    """ View to create a blog post """

    post = BlogPost.objects.get(id=int(id))

    current_info = {
        'blog_title': post.blog_title,
        'content': post.content,
    }
    form = BlogForm(initial=current_info)

    if request.method == 'POST':
        form = BlogForm(request.POST, instance=post)
        if form.is_valid:
            form.save()
            messages.success(request, 'Blog post successfully updated')
            return redirect(reverse('view_blog'))
        else:
            messages.error(request, 'There was an error with the form. Please try again.')
    
    template = 'blog/update_post.html'
    context = {
          'form': form,
      }

    return render(request, template, context)


def delete_post(request, id):
    post = BlogPost.objects.get(id=int(id))
    post.delete()

    return redirect(reverse('view_blog'))

