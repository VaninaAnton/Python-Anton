from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import ConsultaForm
from django.contrib import messages
from django.contrib.auth import logout, login
from .models import Consulta

from .forms import CustomAuthenticationForm, CustomUserCreationForm

def index(request):
    return render(request, 'core/index.html')

def nosotros_view(request):
    return render(request, 'core/nosotros.html')

class CustomLoginView(LoginView):
    redirect_authenticated_user = True
    success_url = reverse_lazy('cliente:index')  # Redirige a la página del cliente después del inicio de sesión


    def get_success_url(self):
        return reverse_lazy('core:index')  # Redirige a la página de inicio después del inicio de sesión

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Guardar el usuario
            username = form.cleaned_data["username"]
            
            # Crear una consulta con los datos del usuario registrado
            consulta = Consulta.objects.create(
                nombre_apellido=username,
                email=user.email,
                telefono='',  # Puedes dejarlo en blanco o solicitarlo en el formulario de registro
                consulta=f'Nuevo registro de usuario: {username}'
            )

            # Autenticar al usuario recién registrado
            login(request, user)
            
            # Mensaje de éxito
            messages.success(request, f"Usuario '{username}' creado correctamente.")

            # Verificación del usuario creado
            print(f"Nuevo usuario creado: {username}")

            # Verificación de la consulta creada
            print(f"Nueva consulta creada: {consulta}")

            # Redirigir a la página de inicio
            return redirect('core:index')
    else:
        form = CustomUserCreationForm()
    return render(request, "core/register.html", {"form": form})


def consulta_view(request):
    if request.method == 'POST':
        form = ConsultaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:consulta_success') 
    else:
        form = ConsultaForm()
    return render(request, 'consulta.html', {'form': form})

def consulta_success_view(request):
    return render(request, 'core/consulta_success.html')

def logout_view(request):
    logout(request)  # Cerrar sesión
    return redirect('core:index')  # Redirigir al usuario a la página principal después del logout