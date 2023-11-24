from rest_framework.serializers import ModelSerializer
from .models import Tienda

class TiendaSerializer(ModelSerializer):
    class Meta:
        model = Tienda
        fields = "__all__"