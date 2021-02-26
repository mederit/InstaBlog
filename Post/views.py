from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm
from django.utils import timezone
from .models import *

def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'Post/posts_list.html', locals())

def post_detail(request, slug):
    post = Post.objects.get(slug__iexact=slug)
    return render(request, 'Post/post_detail.html', locals())

def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('posts_list')
    else:
        form = PostForm()
    return render(request, 'Post/post_create.html', locals())

def update_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.updated_at = timezone.now()
            post.save()
            return redirect('posts_list')
    else:
        form = PostForm()
    return render(request, 'Post/post_update.html', locals())

def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST" and post.author == request.user:
        post.delete()
        return redirect('posts_list')
    return render(request, 'Post/post_delete.html', locals())
    