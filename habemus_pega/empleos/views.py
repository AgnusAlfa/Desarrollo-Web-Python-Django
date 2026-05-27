from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib import messages

from .models import OfertaTrabajo
from .forms import ContactoForm, RegistroForm, OfertaForm

# Modifica tu views.py con estos cambios exactos

# 1. CORRECCIÓN DEL LOGIN: Redirigimos a 'inicio' nuevamente
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.get_user()
            auth_login(request, usuario) 
            # RESTAURAMOS: El login vuelve a enviar a la página de inicio (Dashboard)
            return redirect('inicio')  
    else:
        form = AuthenticationForm()
    
    return render(request, 'registration/login.html', {'form': form})

# 2. CORRECCIÓN DEL EXPLORAR: Quitamos @login_required para que sea público
# De esta forma, cualquier persona puede entrar sin tener que loguearse antes.
def explorar_empleos(request):
    ofertas = OfertaTrabajo.objects.all().order_by('-fecha_publicacion')
    return render(request, 'empleos/explorar.html', {'ofertas': ofertas})


# 2. VISTA DE REGISTRO (Se mantiene igual)
def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistroForm()
    return render(request, 'registration/registro.html', {'form': form})

# 3. VISTA DE LA PÁGINA PRINCIPAL (Dashboard) (Se mantiene con el límite de 3)
@login_required
def inicio(request):
    ofertas = OfertaTrabajo.objects.all().order_by('-fecha_publicacion')[:3]
    return render(request, 'empleos/inicio.html', {'ofertas': ofertas})

# 4. VISTA DE CONTACTO (Se mantiene igual)
@login_required
def contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = ContactoForm()
    return render(request, 'empleos/contacto.html', {'form': form})

# 5. NUEVA VISTA PARA EXPLORAR TODOS LOS EMPLEOS
@login_required 
def explorar_empleos(request):
    ofertas = OfertaTrabajo.objects.all().order_by('-fecha_publicacion')
    return render(request, 'empleos/explorar.html', {'ofertas': ofertas})

# Agrega esta vista al final de tu archivo views.py
@login_required
def publicar_aviso(request):
    if request.method == 'POST':
        form = OfertaForm(request.POST)
        if form.is_valid():
            # Creamos el objeto sin guardarlo en BD aún
            nueva_oferta = form.save(commit=False)
            # Asignamos el autor como el usuario actualmente logueado
            nueva_oferta.autor = request.user 
            # Ahora sí guardamos en la base de datos
            nueva_oferta.save()
            return redirect('explorar') # Redirige a la lista de empleos
    else:
        form = OfertaForm()
    
    return render(request, 'empleos/publicar.html', {'form': form})



