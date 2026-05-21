from django.contrib import admin
from .models import OfertaTrabajo, MensajeContacto

# Registramos nuestros modelos para verlos en el panel de Django
admin.site.register(OfertaTrabajo)
admin.site.register(MensajeContacto)

