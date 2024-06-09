from django.contrib.auth.views import LogoutView  
from django.urls import path
from . import views 

app_name = "core"

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'), 
    path('register/', views.register, name='register'),
    path('nosotros/', views.nosotros_view, name='nosotros'),
    path('consulta/', views.consulta_view, name='consulta'),
    path('consulta/success/', views.consulta_success_view, name='consulta_success'),
]
