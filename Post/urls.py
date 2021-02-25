from django.urls import path, include
from .views import *


urlpatterns = [
    path('posts/', posts_list, name='posts_list'),
]