from django.shortcuts import render
from .forms import ContactoForm  # <--- Importamos nuestro nuevo super formulario

def inicio(request):
    return render(request, 'principal/inicio.html')

def contacto(request):
    mensaje_exito = None

    if request.method == 'POST':
        # Le pasamos los datos que escribió el usuario al formulario de Django
        form = ContactoForm(request.POST)
        
        # ¡Magia! Django revisa automáticamente si el correo tiene @ y si el mensaje tiene 10 caracteres
        if form.is_valid():
            # Si todo está correcto, extraemos el nombre de forma segura
            nombre = form.cleaned_data['nombre']
            mensaje_exito = f"¡Gracias {nombre}! Hemos recibido tu mensaje correctamente."
            # Limpiamos el formulario para que quede en blanco de nuevo
            form = ContactoForm()
    else:
        # Si el usuario recién entra a la página, le mostramos el formulario vacío
        form = ContactoForm()

    # Le enviamos el formulario y el mensaje de éxito a la plantilla HTML
    contexto = {
        'form': form,
        'mensaje_exito': mensaje_exito
    }
    return render(request, 'principal/contacto.html', contexto)



