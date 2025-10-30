from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

def cadastro_usuario(request):
    if request.method == 'POST':
        username = request.POST.get('usuario')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')

        existe_usuario_nome = User.objects.filter(username=username).exists()
        existe_usuario_email = User.objects.filter(email=email).exists()

        if password != password_confirm:
            messages.error(request, "As senhas não coincidem.")
            return redirect('cadastro_usuario')
        try:
            validate_password(password)
        except Exception as e:
            for error in e:
                messages.error(request, error)
            return redirect('cadastro_usuario')

    else:
        return render(request, 'cadastro_usuario.html')

def login(request):
    return render(request, 'login.html')
