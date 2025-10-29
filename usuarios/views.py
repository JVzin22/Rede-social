from django.shortcuts import render
from django.http import HttpResponse

def cadastro_usuario(request):
    return render(request, 'cadastro_usuario.html')

def login(request):
    return render(request, 'login.html')
