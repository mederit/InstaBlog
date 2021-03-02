from django.urls import path
from .views import *


# app_name = 'Post'
urlpatterns = [
    path('', PostListView.as_view(), name='posts_list'),
    path('', recent_post, name='recent_posts'),
    path('post_create/', post_create, name='post_create'),
    path('post/<int:pk>/', post_detail, name='post_detail'),
    path('post/update/<int:pk>/', EditPostView.as_view(), name='post_update'),
    path('post/delete/<int:pk>/', delete_post, name='post_delete'),
    path('get_rules/', RulesView.as_view(), name='rules'),
    path('comment/delete/<int:pk>/', comment_delete, name='comment_delete'),
    path('tags/', TagsListView.as_view(), name='tags_list'),
    path('tag/<str:slug>/', tag_detail, name='tag_detail'),
    path('tag_posts/<str:slug>/', tag_detail1, name='tag_detail1'),

]