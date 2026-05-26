from django.urls import path
from . import views

urlpatterns = [
    # Ruta para la página principal
    path('', views.inicio, name='inicio'),
    
    # Ruta para el formulario de contacto
    path('contacto/', views.contacto, name='contacto'),
    
    # Ruta para iniciar sesión
    path('login/', views.login_view, name='login'),
    
    # Ruta para registrar usuarios nuevos
    path('registro/', views.registro, name='registro'),
]
