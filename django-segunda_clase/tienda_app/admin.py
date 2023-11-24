from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Tienda

# Register your models here.

@admin.register(Tienda)
class TiendaAdmin(ModelAdmin):
    ...

# ->  NEXT vamos alos settings del project settings.py