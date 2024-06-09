from django.urls import path

from producto.views import (
    ProductoCategoriaCreate,
    ProductoCategoriaDelete,
    ProductoCategoriaDetail,
    ProductoCategoriaList,
    ProductoCategoriaUpdate,
    ProductoCreate,
    ProductoDelete,
    ProductoDetail,
    ProductoList,
    ProductoUpdate,
    index,
)

app_name = "producto"

# VISTAS BASADAS EN FUNCIONES
urlpatterns = [
    path("", index, name="index"),
    # path("productocategoria/list", productocategoria_list, name="productocategoria_list"),
    # path("productocategoria/create", productocategoria_create, name="productocategoria_create"),
    # path("productocategoria/detail/<int:pk>", productocategoria_detail, name="productocategoria_detail"),
    # path("productocategoria/update/<int:pk>", productocategoria_update, name="productocategoria_update"),
    # path("productocategoria/delete/<int:pk>", productocategoria_delete, name="productocategoria_delete"),
]

# VISTAS BASADAS EN CLASES
urlpatterns += [
    path("productocategoria/list", ProductoCategoriaList.as_view(), name="productocategoria_list"),
    path("productocategoria/create", ProductoCategoriaCreate.as_view(), name="productocategoria_create"),
    path("productocategoria/detail/<int:pk>", ProductoCategoriaDetail.as_view(), name="productocategoria_detail"),
    path("productocategoria/update/<int:pk>", ProductoCategoriaUpdate.as_view(), name="productocategoria_update"),
    path("productocategoria/delete/<int:pk>", ProductoCategoriaDelete.as_view(), name="productocategoria_delete"),
]

urlpatterns += [
    path("producto/list", ProductoList.as_view(), name="producto_list"),
    path("producto/create", ProductoCreate.as_view(), name="producto_create"),
    path("producto/detail/<int:pk>", ProductoDetail.as_view(), name="producto_detail"),
    path("producto/update/<int:pk>", ProductoUpdate.as_view(), name="producto_update"),
    path("producto/delete/<int:pk>", ProductoDelete.as_view(), name="producto_delete"),
]
