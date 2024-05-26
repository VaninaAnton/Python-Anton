from django.shortcuts import render

from cliente.models import Cliente


def index(request):
    return render(request, "cliente/index.html")


def cliente_list(request):
    consulta = Cliente.objects.all()
    contexto = {"clientes": consulta}
    return render(request, "cliente/cliente_list.html", contexto)
