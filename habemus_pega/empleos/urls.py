from django.urls import path
from . import views


urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('explorar/', views.explorar_empleos, name='explorar'),
    
    # NUEVA RUTA PARA PUBLICAR
    path('publicar/', views.publicar_aviso, name='publicar'),
    
    path('contacto/', views.contacto, name='contacto'),
    path('login/', views.login_view, name='login'),
    path('registro/', views.registro, name='registro'),
]

