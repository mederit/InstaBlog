from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *

def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'Post/posts_list.html', locals())

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments_posts = post.comments_posts.all()
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()
    
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
    if request.method == "POST" and post.author == request.user:
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('posts_list')
    else:
        form = PostForm()
    return render(request, 'Post/post_update.html', locals())


def comment_delete(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post = get_object_or_404(Post, pk=comment.post.pk)
    if request.method == "POST" and post.author == request.user:
        comment.delete()
        return redirect(post.get_absolute_url())
    return render(request, 'Post/comment_delete.html', locals())

