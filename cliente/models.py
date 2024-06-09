from django.db import models

class Pais(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=20, default="")
    fecha_nacimiento = models.DateField(default='2000-01-01')
    contrasena = models.CharField(max_length=100, default='default_value')
    pais_origen = models.CharField(max_length=100, default='')
    foto_perfil = models.ImageField(upload_to='fotos_perfil/', null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"