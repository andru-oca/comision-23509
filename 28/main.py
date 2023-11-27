from Mascota import Mascota
from Mascota import Manager

db:Manager = Manager()

def main():
    pepito:Mascota = Mascota(nombre="pepito",edad=2,)
    gatoben:Mascota = Mascota(nombre="gatoben",edad=10)

    db.insert_mascota(pepito)
    db.insert_mascota(gatoben)

    db.read_db()
    db.save_data()

if __name__ == "__main__":
    main()