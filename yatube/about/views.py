from django.shortcuts import render
# views.py
# Импорт класса TemplateView, чтобы унаследоваться от него
from django.views.generic.base import TemplateView


class JustStaticPage(TemplateView):
    # В переменной template_name обязательно указывается имя шаблона,
    # на основе которого будет создана возвращаемая страница
    template_name = 'about/new.html'