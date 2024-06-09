from django.urls import path
from . import views

app_name = "cliente"

urlpatterns = [
    path('', views.index, name='index'),  # Agrega esta línea para definir la vista 'index'
    path('list/', views.cliente_list, name='cliente_list'), 
    path('nuevo/', views.crear_actualizar_cliente, name='crear_cliente'),
    path('editar/<int:cliente_id>/', views.crear_actualizar_cliente, name='editar_cliente'),
    path('detail/<int:cliente_id>/', views.cliente_detail, name='cliente_detail'), 
    path('register/', views.register, name='register'),
    path('paises/', views.listar_paises, name='listar_paises'),
]
