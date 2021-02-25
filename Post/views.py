from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *


def posts_list(request):
    posts = Post.objects.all()
    post = get_object_or_404(Post)
    comments = post.comments.all()
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
    return render(request, 'Post/posts_list.html', locals())



# def post_detail(request, year, month, day, post):
#     post = get_object_or_404(Post, slug=post,
#                                     status='published',
#                                     publish__year=year,
#                                     publish__month=month,
#                                     publish__day=day)
#     comments = post.comments.all()
#     posts_tags_ids = post.tags.values_list('id', flat=True)
#     similar_posts = Post.objects.filter(tags__in=posts_tags_ids).exclude(id=post.id)
#     similar_posts = similar_posts.annotate(same_tags = Count('tags')).order_by('-same_tags', '-publish')[:4]
#     new_comment = None
#     if request.method == 'POST':
#         comment_form = CommentForm(data=request.POST)
#         if comment_form.is_valid():
#             obj = Comment()
#             obj.body = comment_form.cleaned_data['body']
#             obj.author = request.user
#             obj.post = post
#             obj.save()

#     else:
#         comment_form = CommentForm()


#     return render(request, 'blog/post/detail.html', {'post':post,
#                                                     'similar_posts': similar_posts,
#                                                     'comments': comments,
#                                                     'new_comment': new_comment,
#                                                     'comment_form': comment_form})

# def comment_delete(request, pk):
#     comment = get_object_or_404(Comment, pk=pk)
#     post = get_object_or_404(Post, pk=comment.post.pk)
#     if request.method == "POST" and post.author == request.user:
#         comment.delete()
#         return redirect(post.get_absolute_url())
#     return render(request, 'blog/comment/comment_delete.html', {'comment': comment,
#                                                                 'post': post,
#                                                                 'user': request.user})


