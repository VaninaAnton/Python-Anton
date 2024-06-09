from django.db import models
from django.contrib.auth.models import User

class Pais(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self) -> str:
        return self.nombre

    class Meta:
        verbose_name = "país"
        verbose_name_plural = "países"

class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    nombre = models.CharField(max_length=150)
    apellido = models.CharField(max_length=150)
    nacimiento = models.DateField(null=True, blank=True)
    pais_origen_id = models.ForeignKey(
        Pais, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="país de origen"
    )
    email = models.EmailField(default='default@example.com')  
    telefono = models.CharField(max_length=15, null=True)

    def __str__(self) -> str:
        return f"{self.apellido}, {self.nombre}"

    class Meta:
        verbose_name = "cliente"
        verbose_name_plural = "clientes"
