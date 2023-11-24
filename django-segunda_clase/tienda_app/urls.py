from django.contrib import admin
from django.urls import path , include

from .router import router


from .views import      TiendaListView   \
                    ,   TiendaDetailView \
                    ,   TiendaCreateView \
                    ,   TiendaUpdateView \
                    ,   TiendaDeleteView

app_name = "tienda"

urlpatterns = [
    path("", TiendaListView.as_view(), name="all"),
    path("create/", TiendaCreateView.as_view(), name="create"),
    path("<int:pk>/detail/", TiendaDetailView.as_view(), name="detail"),
    path("<int:pk>/update/", TiendaUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", TiendaDeleteView.as_view(), name="delete")
]

urlpatterns += router.urls