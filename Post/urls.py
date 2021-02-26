from django.urls import path
from .views import *


# app_name = 'Post'
urlpatterns = [
    path('', posts_list, name='posts_list'),
    path('post_create/', post_create, name='post_create'),
    path('post/<str:slug>/', post_detail, name='post_detail'),
    path('post/update/<int:pk>/', update_post, name='post_update'),
    path('post/delete/<int:pk>/', delete_post, name='post_delete'),
]