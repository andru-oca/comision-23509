from .read import read_user
from database import create_user as cu

def create_user(dni:str , db:list[dict]=None)->None:
    if db is None:
        print("che, noru, no me pasaste una db")
        return None

    _user = read_user(dni,db)

    if len(_user) == 0:

        user = cu(
            nombre := input("ingrese nombre\n"), 
            edad := int(input("ingrese edad\n")),
            dni
        )

        _user = user

    print(f"""
    usuario creado:
        {_user["nombre"]}
        {_user["edad"]}
        {_user["dni"]}
    """)

    return
        