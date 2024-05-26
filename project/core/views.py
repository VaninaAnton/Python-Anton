from django.contrib.auth.views import LoginView
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .forms import CustomAuthenticationForm, CustomUserCreationForm


def index(request):
    return render(request, "core/index.html")


def sobre_nosotros(request):
    return render(request, "core/sobre-nosotros.html")

