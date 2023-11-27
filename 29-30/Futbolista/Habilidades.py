class Habilidad:
    def __init__(self,**kwargs):
        self.nombre = kwargs.get("nombre","undefined")
        self.power = kwargs.get("power",100)

    def to_string(self):
        return f"Habilidad: {self.nombre} y estoy en el level: {self.power}"


class Habilidades:
    def __init__(self,**kwargs):
        self.habilidades:list[Habilidad] = kwargs.get("habilidades",[])
    
    def insert_habilidad(self,habilidad: Habilidad)->None:
        self.habilidades.append(habilidad)


class Clubes:
    def __init__(self,**kwargs):
        self.clubes:list[str] = kwargs.get("clubes",[])
    
    def insert_club(self,club)->None:
        self.clubes.append(club)

