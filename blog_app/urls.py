from django.urls import path
from blog_app import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index_page'),
    path('posts/', views.posts_list, name='posts_list'),
    path('posts/<slug:post_slug>/', views.post_detail, name='post_detail'),
    path('categories/', views.category_list, name='category_list'),
    path('categories/<int:category_id>/', views.category_detail, name='category_detail'),
]
