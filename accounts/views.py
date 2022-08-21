from pyexpat.errors import messages
from urllib import request
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .form import LoginForm
from django.contrib import messages
# from django.contrib.auth.forms import UserCreationForm
from .form import SignUpForm

# Create your views here.
def login_view(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                correo = form.cleaned_data.get('correo'),
                password = form.cleaned_data.get('password')
            )
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.info(request, 'Credenciales inválidas')
        else:
            messages.error(request, 'Hay errores en el formulario')
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('index')

def registrar_user(request):
    form = SignUpForm()
    if request.method== 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            messages.success(request, 'Usuario creado!')
            return redirect('login')
    return render(request, 'accounts/register.html', {'form': form})
