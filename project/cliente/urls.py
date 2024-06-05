from django.urls import path
from .views import home, registro, login_view, logout_view, consulta

urlpatterns = [
    path('', home, name='home'),
    path('registro/', registro, name='registro'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('consulta/', consulta, name='consulta'),
]
