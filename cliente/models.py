from django.db import models

class Pais(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self) -> str:
        return self.nombre

    class Meta:
        verbose_name = "país"
        verbose_name_plural = "países"


class Cliente(models.Model):
    nombre = models.CharField(max_length=150)
    apellido = models.CharField(max_length=150)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    contrasena = models.CharField(max_length=150)  # Esto puede no ser seguro, considera usar un campo más seguro como PasswordField
    pais_origen = models.ForeignKey(
        Pais, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="país de origen"
    )
    foto_perfil = models.ImageField(upload_to='perfil/', null=True, blank=True)

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"

    class Meta:
        verbose_name = "cliente"
        verbose_name_plural = "clientes"
