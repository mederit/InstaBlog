from django.urls import path, include
from .views import *


urlpatterns = [
    path('posts/', ),
    path('comment/delete/<int:pk>/', comment_delete, name='comment_delete'),
]