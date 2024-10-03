from django.urls import path
from .views import post_view
from django.shortcuts import render

urlpatterns = [
    path('', post_view, name='post_view'),  # Rota para a view atual
    path('index/', lambda request: render(request, 'index.html'), name='index'),  # Rota para o template index.html
]
