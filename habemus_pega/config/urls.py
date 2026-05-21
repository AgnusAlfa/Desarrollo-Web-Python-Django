from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cuentas/', include('django.contrib.auth.urls')), 
    # Conectamos las rutas de nuestra aplicación
    path('', include('empleos.urls')), 
]
