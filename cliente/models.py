from django.contrib.auth.models import AbstractUser
from django.db import models

class Pais(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class CustomUser(AbstractUser): 
    telefono = models.CharField(max_length=20, default="")
    fecha_nacimiento = models.DateField(default='2000-01-01')
    pais_origen = models.ForeignKey(Pais, on_delete=models.SET_NULL, null=True, blank=True)
    foto_perfil = models.ImageField(upload_to='fotos_perfil/', null=True, blank=True)

    def __str__(self):
        return f"{self.username}"
