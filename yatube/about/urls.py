# файл about/urls.py
from django.urls import path
from . import views


app_name = 'about'

urlpatterns = [
    path('author/', views.JustStaticPage.as_view()),
    path('tech/', views.JustStaticPage.as_view()),
] 