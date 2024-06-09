from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import get_user_model

class CustomAuthenticationForm(AuthenticationForm):
    pass  # No necesitamos definir Meta ya que AuthenticationForm ya contiene los campos necesarios

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()  
        fields = ["username", "password1", "password2"]



# formulario página de inicio
from django import forms
from .models import Consulta

class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = ['nombre_apellido', 'email', 'telefono', 'consulta']
