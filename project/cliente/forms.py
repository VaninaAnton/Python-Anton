from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Cliente

class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = Cliente
        fields = ("username", "email", "password1", "password2")

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
