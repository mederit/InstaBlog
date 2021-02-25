from django.urls import path
from .views import *

urlpatterns = [
    path('', posts_list, name='posts_list'),
    path('post_create/', post_create, name='post_create'),
    path('post/<str:slug>/', post_detail, name='post_detail'),
    path('post/update/<int:pk>/', update_post, name='post_update'),
]