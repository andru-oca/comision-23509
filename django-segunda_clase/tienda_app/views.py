from django.urls import reverse_lazy
from django.views import View

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView


from .models import Tienda

# Create your views here.


class TiendaBaseView(View):
    template_name = 'tienda.html'
    model = Tienda
    fields = '__all__'
    success_url = reverse_lazy('tienda:all')


class TiendaListView(TiendaBaseView,ListView):
    """
    ESTO ME PERMITE CREAR UNA VISTA CON LOS Tienda
    """

class TiendaDetailView(TiendaBaseView,DetailView):
    template_name = "tienda_detail.html"

class TiendaCreateView(TiendaBaseView,CreateView):
    template_name = "tienda_create.html"
    extra_context = {
        "tipo": "Crear tienda"
    }

class TiendaUpdateView(TiendaBaseView,UpdateView):
    template_name = "tienda_create.html"
    extra_context = {
        "tipo": "Actualizar tienda"
    }

class TiendaDeleteView(TiendaBaseView,DeleteView):
    template_name = "tienda_delete.html"
    extra_context = {
        "tipo": "Borrar tienda"
    }
