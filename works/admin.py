from django.contrib import admin
from .models import TrabajoEnCurso, TrabajoFinalizado

@admin.register(TrabajoEnCurso)
class TrabajoEnCursoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'estado', 'fecha_ingreso', 'fecha_retiro', 'presupuesto')

@admin.register(TrabajoFinalizado)
class TrabajoFinalizadoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'fecha_retiro', 'observaciones')
