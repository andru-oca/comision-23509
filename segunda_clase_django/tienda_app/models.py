from django.db import models
from django.db.models import Model

# Create your models here.
class Tienda(Model):
    """
    Atributos de clase que son usadas por herencia de la clase Model
    """


    rubros_choices = [
        ('comida',"Gastronomia"),
        ("industria","Industria Textil"),
        ("golosinas","Chucherias")
    ]

    nombre = models.CharField(max_length=100,default="tienda x")
    ubicacion = models.CharField(max_length=100,default="calle falsa 123")
    precio_tienda = models.FloatField(null=False, blank=False, default=128_000.00)
    contacto = models.EmailField(max_length=100,default="tienda_x@mail.com")
    rubro = models.CharField(max_length=10, choices=rubros_choices)
    fecha_disponible = models.DateField(auto_now=True)

    # podemos crear la tabla con un nombre especifico pero se lo tenemos
    # que indicar directamente en la metaclase

    class Meta:
       db_table = "tiendas_cordoba_ventas"


    def __str__(self):
        return f"La tienda {self.nombre} es del rubro {self.rubro}"

    def get_fields(self):
        return [
            (field.verbose_name, field.value_from_object(self))
            for field in self.__class__._meta.fields[1:]
        ]
    
# -> NEXT -> registrar el modelo en  admin.py