from django.contrib import admin
from django.urls import path
from django.urls import include

from .views import Index

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", Index.as_view(), name="index"),
    path("tienda/", include("tienda_app.urls"))
]