from Mascota import Mascota

class Manager:
    def __init__(self,**kwargs):
        self.db = kwargs.get("db",[])

    def read_db(self):
        if isinstance(self.db,list):
            for mascota in self.db:
                print(mascota)
    
    def insert_mascota(self,mascota:Mascota=None):
        if mascota:
            self.db.append(mascota)
            print(f"Ingresó la mascota: {mascota.id}")
    def save_data(self):
        if isinstance(self.db,list):
            db_texto:str = ''

            for mascota in self.db:
                db_texto += mascota.to_string()

            with open("base_generica.txt","w",encoding="latin-1") as file:
                file.write(db_texto)
