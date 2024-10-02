from django.db import models
from django.contrib.auth.models import User

# Definindo as opções de status
STATUS = (
    (0, "Draft"),  # Rascunho
    (1, "Publish")  # Publicado
)

# Criando o modelo de Post
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)  # Título do post, único
    slug = models.SlugField(max_length=200, unique=True)   # Slug único para URL amigável
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')  # Relacionando com o modelo de usuário
    updated_on = models.DateTimeField(auto_now=True)  # Data de atualização automática
    content = models.TextField()  # Conteúdo do post
    created_on = models.DateTimeField(auto_now_add=True)  # Data de criação do post
    status = models.IntegerField(choices=STATUS, default=0)  # Status: rascunho ou publicado

    class Meta:
        ordering = ['-created_on']  # Ordena os posts pela data de criação (mais recentes primeiro)

    def __str__(self):
        return self.title  # Retorna o título do post como representação do objeto
