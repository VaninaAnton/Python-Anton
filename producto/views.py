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


# ***** PRODUCTOCATEGORIA

# LIST
# def productocategoria_list(request):
#     busqueda = request.GET.get("busqueda", None)
#     if busqueda:
#         print(busqueda)
#         consulta = ProductoCategoria.objects.filter(nombre__icontains=busqueda)
#     else:
#         consulta = ProductoCategoria.objects.all()
#     contexto = {"productocategoria": consulta}
#     return render(request, "producto/productocategoria_list.html", contexto)


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


# CREATE
# def productocategoria_create(request):
#     if request.method == "POST":
#         form = ProductoCategoriaForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("producto:productocategoria_list")
#     else:  # GET
#         form = ProductoCategoriaForm()
#     return render(request, "producto/productocategoria_form.html", {"form": form})


class ProductoCategoriaCreate(CreateView):
    model = ProductoCategoria
    form_class = ProductoCategoriaForm
    success_url = reverse_lazy("producto:productocategoria_list")


# DETAIL
# def productocategoria_detail(request, pk: int):
#     consulta = ProductoCategoria.objects.get(id=pk)
#     contexto = {"producto": consulta}
#     return render(request, "producto/productocategoria_detail.html", contexto)


class ProductoCategoriaDetail(DetailView):
    model = ProductoCategoria


# UPDATE
# def productocategoria_update(request, pk: int):
#     consulta = ProductoCategoria.objects.get(id=pk)
#     if request.method == "POST":
#         form = ProductoCategoriaForm(request.POST, instance=consulta)
#         if form.is_valid():
#             form.save()
#             return redirect("producto:productocategoria_list")
#     else:  # GET
#         form = ProductoCategoriaForm(instance=consulta)
#     return render(request, "producto/productocategoria_form.html", {"form": form})


class ProductoCategoriaUpdate(UpdateView):
    model = ProductoCategoria
    form_class = ProductoCategoriaForm
    success_url = reverse_lazy("producto:productocategoria_list")


# DELETE
# def productocategoria_delete(request, pk: int):
#     consulta = ProductoCategoria.objects.get(id=pk)
#     if request.method == "POST":
#         consulta.delete()
#         return redirect("producto:productocategoria_list")
#     return render(request, "producto/productocategoria_confirm_delete.html", {"object": consulta})


class ProductoCategoriaDelete(DeleteView):
    model = ProductoCategoria
    success_url = reverse_lazy("producto:productocategoria_list")


# ***** PRODUCTO


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
