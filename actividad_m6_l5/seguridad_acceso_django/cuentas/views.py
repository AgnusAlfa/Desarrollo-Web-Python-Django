from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

# 1. Guardia Estándar: Solo deja pasar a los que iniciaron sesión
class InicioView(LoginRequiredMixin, TemplateView):
    template_name = 'inicio.html'

# 2. Guardia VIP: Solo deja pasar a los que tienen un permiso especial
class SeccionSecretaView(PermissionRequiredMixin, TemplateView):
    template_name = 'secreta.html'
    # Pedimos un permiso que tu superusuario ya tiene por defecto
    permission_required = 'auth.view_user'
    