from .read import read_user
from .delete import delete_user

def update_user(dni:str, db:list[dict]=None)->None:
    if db is None:
        print("che, noru, no me pasaste una db")
        return None

    _user:dict = read_user(dni,db)

    if _user is None or len(_user) == 0 :
        print("No ha usuario disponible")
        return
    
    key:str = input("ingrese el campo a modificar:\n campos disponibles a cambio\n*email:\n*nombre\n*edad\n") 
    value:str = input("ingrese el valor modificado")


    _user[key] = value

    delete_user(dni,db)

    db.append(_user)

    print("usuario guardado")

