from django.db import models

class Consulta(models.Model):
    nombre_apellido = models.CharField(max_length=255)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    consulta = models.TextField()
    fecha_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre_apellido} - {self.email}"
