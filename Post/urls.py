from django.urls import path
from .views import *

urlpatterns = [
    path('', posts_list, name='posts_list'),
    path('post_create/', post_create, name='post_create'),
    path('post/<int:pk>/', post_detail, name='post_detail'),
    path('post/update/<int:pk>/', update_post, name='post_update'),
    path('comment/delete/<int:pk>/', comment_delete, name='comment_delete'),
]