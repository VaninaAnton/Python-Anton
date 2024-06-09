from django.contrib import admin
from .models import CustomUser, Pais

admin.site.register(CustomUser) 
admin.site.register(Pais)