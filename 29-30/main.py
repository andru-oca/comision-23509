from Futbolista import FutbolistaArgentino ,FutbolistaMexicano
from Futbolista import Habilidad

def main():
    cubero:FutbolistaArgentino = FutbolistaArgentino(
            nombre="fabian" ,clubes=["Velez"]

    )

    print(cubero)
    cubero.get_name()

    cubero.insert_habilidad(Habilidad(nombre="super patada"))
    cubero.insert_habilidad(Habilidad(nombre="tiro del dragon",power=200))


    print(cubero.habilidades)


    cubero.insert_club("Tigre")
    cubero.insert_club("Barcelon")

    print(cubero.clubes)


    chicharito:FutbolistaMexicano = FutbolistaMexicano()
    chicharito.get_name()
if __name__ == "__main__":
    main()