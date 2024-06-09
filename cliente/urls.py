from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cliente.urls', namespace='cliente')),  
    path("list/", cliente_list, name="cliente_list"),
    path("detail/", cliente_detail, name="cliente_detail"),
]
