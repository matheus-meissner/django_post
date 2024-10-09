from django.urls import path
from .views import post_view, post_detail

urlpatterns = [
    path('', post_view, name='home'),
    path('post/<slug:slug>/', post_detail, name='post_detail'),  # Definindo a URL para os detalhes do post
]
