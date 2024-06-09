from django import forms
from .models import CustomUser


class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = CustomUser 
        fields = ['username', 'email', 'password'] 

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

class ClienteForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'telefono', 'fecha_nacimiento', 'pais_origen', 'foto_perfil']