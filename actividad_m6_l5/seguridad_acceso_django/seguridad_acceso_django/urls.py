from django.contrib import admin
from django.urls import path, include
from cuentas.views import InicioView # <--- Importamos nuestro guardia de seguridad

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cuentas/', include('django.contrib.auth.urls')),
    
    # Esta será nuestra página de inicio protegida
    path('', InicioView.as_view(), name='inicio'), 
]
