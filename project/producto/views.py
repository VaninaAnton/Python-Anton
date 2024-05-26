from typing import Any

from django.db.models import Q
from django.db.models.query import QuerySet
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from producto.forms import ProductoCategoriaForm, ProductoForm
from producto.models import Producto, ProductoCategoria


def index(request):
    return render(request, "producto/index.html")


# PRODUCTO CATEGORIA
# LISTA
class ProductoCategoriaList(ListView):
    model = ProductoCategoria
    # context_object_name = "productocategoria"
    # template_name = "producto/list.html"

    def get_queryset(self) -> QuerySet[Any]:
        queryset = super().get_queryset()
        busqueda = self.request.GET.get("busqueda")
        if busqueda:
            queryset = ProductoCategoria.objects.filter(
                Q(nombre__icontains=busqueda) | Q(descripcion__icontains=busqueda)
            )
        return queryset


# CREAR
class ProductoCategoriaCreate(CreateView):
    model = ProductoCategoria
    form_class = ProductoCategoriaForm
    success_url = reverse_lazy("producto:productocategoria_list")


# DETALLE
class ProductoCategoriaDetail(DetailView):
    model = ProductoCategoria


# ACTUALIZAR
class ProductoCategoriaUpdate(UpdateView):
    model = ProductoCategoria
    form_class = ProductoCategoriaForm
    success_url = reverse_lazy("producto:productocategoria_list")


# ELIMINAR
class ProductoCategoriaDelete(DeleteView):
    model = ProductoCategoria
    success_url = reverse_lazy("producto:productocategoria_list")


# PRODUCTO
class ProductoList(ListView):
    model = Producto

    def get_queryset(self) -> QuerySet[Any]:
        queryset = super().get_queryset()
        busqueda = self.request.GET.get("busqueda")
        if busqueda:
            queryset = Producto.objects.filter(nombre__icontains=busqueda)
        return queryset


class ProductoCreate(CreateView):
    model = Producto
    form_class = ProductoForm
    success_url = reverse_lazy("producto:producto_list")


class ProductoDetail(DetailView):
    model = Producto


class ProductoUpdate(UpdateView):
    model = Producto
    form_class = ProductoForm
    success_url = reverse_lazy("producto:producto_list")


class ProductoDelete(DeleteView):
    model = Producto
    success_url = reverse_lazy("producto:producto_list")
