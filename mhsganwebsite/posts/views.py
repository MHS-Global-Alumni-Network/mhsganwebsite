from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from .models import Post

# Create your views here.
@login_required
def create_post(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.created_by = request.user
            post.save()
            return redirect('posts_list')
    else:
        post_form = PostForm()
    return render(request, 'posts/create_post.html', {'form': post_form})


def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'posts/posts.html', {'posts': posts})
