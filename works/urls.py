from django.urls import path
from . import views

app_name = 'works'

urlpatterns = [
    path('trabajos/', views.trabajos_view, name='trabajos'),
]
