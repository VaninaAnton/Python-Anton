from django.urls import path
from . import views

app_name = "cliente"

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.cliente_list, name='cliente_list'), 
    path('detail/<int:cliente_id>/', views.cliente_detail, name='cliente_detail'), 
    path('register/', views.register, name='register'),
]
