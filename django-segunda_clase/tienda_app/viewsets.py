from rest_framework.viewsets import ModelViewSet
from .models import Tienda
from .serializers import TiendaSerializer

class TiendaViewSet(ModelViewSet):
    queryset = Tienda.objects.all()
    serializer_class = TiendaSerializer