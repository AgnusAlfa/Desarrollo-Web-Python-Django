from django.contrib.auth.models import User
from django.db import models

class OfertaTrabajo(models.Model):
    titulo = models.CharField(max_length=200, verbose_name="Título del Cargo")
    empresa = models.CharField(max_length=100, verbose_name="Nombre de la Empresa")
    descripcion = models.TextField(verbose_name="Descripción del Cargo")
    ubicacion = models.CharField(max_length=100, verbose_name="Ubicación / Ciudad")
    salario = models.CharField(max_length=100, blank=True, null=True, verbose_name="Salario (Opcional)")
    fecha_publicacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Publicación")
    # Este es el campo nuevo que vincula la oferta con el usuario (autor)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Autor")

    def __str__(self):
        return f"{self.titulo} - {self.empresa}"

class MensajeContacto(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre del Reclutador o Empresa")
    correo = models.EmailField(verbose_name="Correo Electrónico")
    asunto = models.CharField(max_length=200, verbose_name="Asunto")
    mensaje = models.TextField(verbose_name="Mensaje / Detalle de la vacante")
    fecha_envio = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Envío")

    def __str__(self):
        return f"Mensaje de {self.nombre} - {self.asunto}"
    
