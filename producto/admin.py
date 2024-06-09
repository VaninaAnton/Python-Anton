from django.contrib import admin

# Register your models here.
from .models import Producto, ProductoCategoria


class ProductoAdmin(admin.ModelAdmin):
    list_display = (
        "categoria_id",
        "nombre",
        "unidad_de_medida",
        "cantidad",
        "precio",
        "fecha_actualizacion",
    )
    list_display_links = ("nombre",)
    list_filter = ("categoria_id",)
    date_hierarchy = "fecha_actualizacion"


admin.site.register(ProductoCategoria)
admin.site.register(Producto, ProductoAdmin)
