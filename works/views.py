from django.shortcuts import render
from .models import TrabajoEnCurso, TrabajoFinalizado

def trabajos_view(request):
    trabajos_en_curso = TrabajoEnCurso.objects.all()
    trabajos_finalizados = TrabajoFinalizado.objects.all()
    return render(request, 'work/trabajos.html', {
        'trabajos_en_curso': trabajos_en_curso,
        'trabajos_finalizados': trabajos_finalizados
    })
