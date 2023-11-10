# ------------functions


# def greeting(nombre:str = "stranger") -> str:
    # print(f"Hola, {nombre}")
    # return f"Hola, {nombre}"

# saludo:str = greeting("Adrian")

# greeting( nombre := input("Ingrese el nombre a saludar \n") )

# print(nombre)


# ------------ CRUD

"""
- base_datos => crear usuario | crear multiples usuarios

- que operacion de CRUD queres hacer?

- CONTROLLERS :: logica {
    -create
    -read
    -update
    -delete
}

que definis hacer despues de aplicar la operacion

"""
from database import create_database
from controllers import read_user
from controllers import create_user
from controllers import delete_user

db_users:list[dict] = create_database() 
print(db_users)

def main():
    opcion:str = input("""
Bienvenido a nuestro gestor de usuarios

          opcion a => crear usuario
          opcion b => leer usuario    
          opcion c => actualizar usuario    
          opcion d => borrar usuario    
""")

    if opcion == "a":
        create_user(dni := input("ingrese dni \n") ,db_users)
        return 
    if opcion == "b":
        read_user( dni := input("ingrese dni \n") ,db_users )
        return 
    if opcion == "d":
        print(id(db_users))
        print(len(db_users))
        delete_user( dni := input("ingrese dni \n") ,db_users )
        print(len(db_users))
        return 


main()


