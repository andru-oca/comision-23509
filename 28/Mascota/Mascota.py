import uuid

class Mascota(object):
    # attr de clase
    tipo_animal:str = "perro"
    _sonido:str = "guau 🐕‍🦺"

    # parametros dinamicos *args y **kwargs 

    def __init__(self,**kwargs) -> None:
        self.id = str(uuid.uuid4())
        self.raza = kwargs.get("raza")
        self.edad = kwargs.get("edad")
        self.nombre = kwargs.get("nombre")
        self.__modificar_tipo_animal(tipo_animal := input(f"{self.nombre}: cambia el tipo por defecto? a que animal?:\n"))

    def __modificar_tipo_animal(self,tipo_animal:str=None):
        if tipo_animal:
            self.tipo_animal = tipo_animal
            return 


    def __str__(self) -> str:
        return f"""
        Soy un {self.tipo_animal}
        Tengo {self.edad}
        Mi nombre es {self.nombre}
        """

    def to_string(self)->str:
        return f"""
        >>>
        Codigo ID mascota: {self.id}
        Soy un {self.tipo_animal}
        Tengo {self.edad}
        Mi nombre es {self.nombre}
        >>>>

        """

    # metodos
    def sonido(self)->None:
        print(f"Esta mascota del tipo {self.tipo_animal} hace {self._sonido}")
