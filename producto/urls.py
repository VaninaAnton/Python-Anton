from django.urls import path
from . import views

app_name = "trabajos"

urlpatterns = [
    path('', views.trabajos, name='trabajos'),
]
