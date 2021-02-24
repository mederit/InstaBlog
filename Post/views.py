from django.shortcuts import render
from .models import *

def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'Post/posts_list.html', locals())
