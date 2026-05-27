from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib import messages

from .models import OfertaTrabajo
from .forms import ContactoForm, RegistroForm


# 1. VISTA DE LOGIN
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.get_user()
            auth_login(request, usuario) # Inicia la sesión del usuario
            return redirect('inicio')    # Lo manda al dashboard
    else:
        form = AuthenticationForm()
    
    # MODIFICADO: Ahora respeta tu estructura y apunta a 'registration/login.html'
    return render(request, 'registration/login.html', {'form': form})


# 2. VISTA DE REGISTRO
def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistroForm()
    return render(request, 'registration/registro.html', {'form': form})


# 3. VISTA DE LA PÁGINA PRINCIPAL (Dashboard)
@login_required
def inicio(request):
    ofertas = OfertaTrabajo.objects.all().order_by('-fecha_publicacion')
    # Mantiene su ruta original, que está correcta en tu estructura
    return render(request, 'empleos/inicio.html', {'ofertas': ofertas})


# 4. VISTA DE CONTACTO
@login_required
def contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save() # Guarda el mensaje en la base de datos
            return redirect('inicio')
    else:
        form = ContactoForm()
    
    # Mantiene su ruta original, que está correcta en tu estructura
    return render(request, 'empleos/contacto.html', {'form': form})
