from django.db import models
from django.utils import timezone


class ProductoCategoria(models.Model):
    """Categorías de productos"""

    nombre = models.CharField(max_length=200, unique=True)
    descripcion = models.TextField(
        null=True,
        blank=True,
        verbose_name="descripción",
    )

    def __str__(self) -> str:
        """Retorna una instancia del modelo en forma de cadena de texto"""
        return self.nombre

    class Meta:
        verbose_name = "categoría de producto"
        verbose_name_plural = "categorías de producto"


class Producto(models.Model):
    categoria_id = models.ForeignKey(ProductoCategoria, null=True, blank=True, on_delete=models.SET_NULL)
    nombre = models.CharField(max_length=200)
    unidad_de_medida = models.CharField(max_length=200)
    cantidad = models.FloatField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField(null=True, blank=True, verbose_name="descripción")
    fecha_actualizacion = models.DateField(null=True, blank=True, editable=False, default=timezone.now)

    def __str__(self) -> str:
        return f"{self.nombre} ({self.unidad_de_medida}) ${self.precio:.2f}"

    class Meta:
        verbose_name = "producto"
        verbose_name_plural = "productos"
