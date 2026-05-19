from django.shortcuts import render

# Esta es tu vista de la página de inicio
def inicio(request):
    return render(request, 'principal/inicio.html')

# Esta es tu nueva vista para la página de contacto con validación Backend
def contacto(request):
    # Variables para guardar nuestros mensajes
    mensaje_exito = None
    mensaje_error = None

    # Verificamos si el usuario presionó el botón "Enviar" (Método POST)
    if request.method == 'POST':
        # Capturamos lo que el usuario escribió en las cajas de texto
        nombre_usuario = request.POST.get('nombre', '')
        email_usuario = request.POST.get('email', '')

        # VALIDACIÓN BACKEND: Verificamos que no vengan vacíos
        if nombre_usuario == '' or email_usuario == '':
            mensaje_error = "Error: ¡Todos los campos son obligatorios!"
        else:
            mensaje_exito = f"¡Gracias {nombre_usuario}! Hemos recibido tu mensaje correctamente."

    # Finalmente, mostramos la página de contacto enviándole los mensajes (si los hay)
    contexto = {
        'mensaje': mensaje_exito,
        'error': mensaje_error
    }
    return render(request, 'principal/contacto.html', contexto)




