from django.shortcuts import render
from .models import Trabajo

def trabajos(request):
    cliente = request.user
    trabajos_en_curso = Trabajo.objects.filter(cliente=cliente, en_curso=True)
    trabajos_pasados = Trabajo.objects.filter(cliente=cliente, en_curso=False)
    return render(request, 'cliente/trabajos.html', {'trabajos_en_curso': trabajos_en_curso, 'trabajos_pasados': trabajos_pasados})
