from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import OfertaTrabajo
from .forms import ContactoForm

# Vista de la página principal (Dashboard)
@login_required
def inicio(request):
    ofertas = OfertaTrabajo.objects.all().order_by('-fecha_publicacion')
    return render(request, 'empleos/inicio.html', {'ofertas': ofertas})

# Vista del formulario de contacto avanzado
@login_required
def contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save() # Guarda el mensaje en la base de datos
            return redirect('inicio')
    else:
        form = ContactoForm()
    
    return render(request, 'empleos/contacto.html', {'form': form})

