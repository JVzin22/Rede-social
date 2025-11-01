from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now as Now

class Estado(models.Model):
    nome = models.CharField(max_length=50, null=False, blank=False)
    uf = models.CharField(max_length=2, null=False, blank=False)
    data_cadastro = models.DateTimeField(auto_now_add=True, null=False, blank=False)

    def __str__(self):
        return self.nome

class Cidade(models.Model):
    nome = models.CharField(max_length=50, null=False, blank=False)
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT, null=False, blank=False)
    data_cadastro = models.DateTimeField(auto_now_add=True, null=False, blank=False)

    def __str__(self):
        return self.nome

class Usuario(AbstractUser):
    foto_perfil = models.ImageField(upload_to='perfil', null=True, blank=True)
    biografia = models.TextField(max_length=500, null=True, blank=True)
    cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT, null=True, blank=True)
    data_nascimento = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.username

class Postagem(models.Model):
    titulo = models.CharField(max_length=100, null=False, blank=False)
    imagem = models.ImageField(upload_to='postagem', null=False, blank=False)
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT, null=False, blank=False)
    data_cadastro = models.DateTimeField(auto_now_add=True, null=False, blank=False)

    def __str__(self):
        return self.titulo
