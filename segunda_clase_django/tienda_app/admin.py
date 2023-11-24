from .models import Tienda
from django.contrib import admin
from django.contrib.admin import ModelAdmin

# Register your models here.


@admin.register(Tienda)
class TiendaAdmin(ModelAdmin):
    ...

# NEXT ->  settings del projecto 
