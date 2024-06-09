from django.db import models

class TrabajoEnCurso(models.Model):
    codigo = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    fecha_ingreso = models.DateField()
    fecha_retiro = models.DateField(null=True, blank=True)
    presupuesto = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.codigo

class TrabajoFinalizado(models.Model):
    codigo = models.CharField(max_length=100)
    fecha_retiro = models.DateField()
    observaciones = models.TextField()

    def __str__(self):
        return self.codigo
