from .FutbolistaAbstracto import Futbolista
from .Habilidades import Habilidades ,Clubes


class FutbolistaArgentino(Futbolista,Habilidades,Clubes):

    def __init__(self,**kwargs) -> None:
        self.nombre = kwargs.get("nombre", "sin_nombre")
        self.mate = kwargs.get("mate", True)
        self.nacionalidad = kwargs.get("nacionalidad", "argentino")

        # super().__init__(**kwargs)
        Habilidades.__init__(self,**kwargs)
        Clubes.__init__(self,**kwargs)

    def __str__(self):
        return f"""
        hola, soy {self.nombre}
        { 'Tomo mate' if {self.mate} else "No tomo mate"}
        tengo la nacionalidad {self.nacionalidad}
    """
    
    def get_name(self):
        print(f"soy un futbolista de {self.nacionalidad}, yo tomo mate, y digo che")
    
    def hablar_sin_s(self):
        ...


class FutbolistaMexicano(Futbolista):

    def get_name(self):
        lugar_origen:str = "mexicali"

        print(f"soy un futbolista de viva mexico de {lugar_origen}, y como tacos picantes")
    
    def hablar_sin_s(self):
        ...
