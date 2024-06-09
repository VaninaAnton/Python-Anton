from django.urls import path

from cliente.views import cliente_list, index

app_name = "cliente"

urlpatterns = [
    path("", index, name="index"),
    path("cliente/list", cliente_list, name="cliente_list"),
]
