from django.shortcuts import render, get_object_or_404
from .models import Post  # Certifique-se de importar seu modelo Post

def post_view(request):
    posts = Post.objects.all()  # Recupera todos os posts do banco de dados
    return render(request, 'index.html', {'post_list': posts})  # Passa a lista de posts para o template

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)  # Recupera o post correspondente ao slug
    return render(request, 'post_detail.html', {'post': post})  # Renderiza o template com os detalhes do post
