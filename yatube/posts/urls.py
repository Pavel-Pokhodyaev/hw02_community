# posts/urls.py
from django.urls import path, include
from . import views

app_name = 'posts'

urlpatterns = [
    # Главная страница
    path('', views.index, name='index'),
    # Профайл пользователя
    path('profile/<str:username>/', views.profile, name='profile'),
    # Просмотр записи
    path('posts/<int:post_id>/', views.post_detail, name='post_detail'),
    # Страница со списком постов
    #path('index.html', views.index),
    path('group/<slug:slug>/', views.group_posts, name='group_list'),
    #path('about/', include('about.urls', namespace='about'))
    path('post/create/', views.post_create, name='post_create'),
]
