from django.contrib.auth.views import LogoutView
from django.urls import path

from core.views import index, sobre_nosotros

app_name = "core"

urlpatterns = [
    path("", index, name="index"),
    path("logout/", LogoutView.as_view(template_name="core/logout.html"), name="logout"),
    path("sobre-nosotros/", sobre_nosotros, name= "nosotros"),
]
