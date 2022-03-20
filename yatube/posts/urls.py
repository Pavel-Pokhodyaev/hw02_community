# posts/urls.py
from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    # Главная страница
    path('', views.index, name='index'),
    # Страница со списком постов
    path('index.html', views.index),
    path('group/<slug:slug>/', views.group_posts, name='group_list'),
    path('group_list/<slug:slug>', views.group_posts, name='group_list')
]
