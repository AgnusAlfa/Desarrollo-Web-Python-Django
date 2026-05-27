from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import MensajeContacto

class ContactoForm(forms.ModelForm):
    class Meta:
        model = MensajeContacto
        fields = ['nombre', 'correo', 'asunto', 'mensaje']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Empresa S.A.'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'contacto@empresa.com'}),
            'asunto': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Publicar nueva vacante'}),
            'mensaje': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Detalles de la oferta...'}),
        }

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistroForm(UserCreationForm):
    # Agregamos el campo correo manualmente para que aparezca
    email = forms.EmailField(label="Correo", required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email") # Django agrega automáticamente Contraseña y Confirmar

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Aplicamos tus clases CSS a todos los campos
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
        
        # Opcional: Traducimos los labels de las contraseñas
        self.fields['username'].label = "Usuario"
        self.fields['password1'].label = "Contraseña"
        self.fields['password2'].label = "Confirmar Contraseña"
        

