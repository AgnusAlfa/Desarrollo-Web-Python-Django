from django import forms

class ContactoForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    correo = forms.EmailField()
    mensaje = forms.CharField(
        widget=forms.Textarea, 
        min_length=10,
        error_messages={'min_length': 'El mensaje debe tener al menos 10 caracteres.'}
    )

