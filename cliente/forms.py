from django import forms
from cliente.models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'email', 'telefono', 'fecha_nacimiento', 'contrasena', 'pais_origen', 'foto_perfil']
