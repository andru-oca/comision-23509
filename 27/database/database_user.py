import random

_nombres:list[str] = ["Erik", "Ingrid", "Olaf", "Maja", "Lars", "Sigrid", "Hans", "Ida"]

_dni:list[str] = [str(random.randint(50_000_000, 86_000_000)) for _ in range(200)]
_edad:list[int] = [random.randint(29, 86) for _ in range(20)]

def generar_correo_noruego(nombre):
    dominios_noruegos = ["gmail.com", "hotmail.com", "outlook.com", "yahoo.no", "live.no", "one.com", "getmail.no", "online.no", "webmail.no"]
    dominio = random.choice(dominios_noruegos)
    correo = nombre.lower() + "@" + dominio
    return correo

def create_user(nombre:str = None, edad:int=None, dni:str = None)->dict:

    """
    Crea un diccionario representando un usuario con información opcional.

    Parameters:
    - nombre (str, optional): El nombre del usuario. Si no se proporciona, se elige aleatoriamente de la lista de nombres noruegos.
    - edad (int, optional): La edad del usuario. Si no se proporciona, se elige aleatoriamente.
    - dni (str, optional): El número de identificación del usuario. Si no se proporciona, se elige aleatoriamente.

    Returns:
    dict: Un diccionario que contiene la información del usuario con las claves "nombre", "email", "edad" y "dni".
          Si no se proporcionan valores para nombre, edad y dni, se eligen aleatoriamente.

    Example:
    >>> create_user()
    {'nombre': 'NombreAleatorio', 'email': 'correo@noruego.com', 'edad': 25, 'dni': '123456789'}
    """


    nombre:str = random.choice(_nombres) if nombre is None  else nombre
    edad:int = random.choice(_edad) if edad is None else edad
    dni:str = random.choice(_dni) if dni is None else dni

    return  {
            "nombre":   nombre,
            "email":    generar_correo_noruego(nombre),
            "edad": edad,
            "dni" : dni
        }



def create_database(cant_usuarios:int=10)->list[dict]:
    """
    Crea una base de datos de usuarios aleatorios.
    Args:
        cant_usuarios (int, opcional): La cantidad de usuarios a crear. Por defecto, 10.
    Returns:
        list[dict]: Una lista de diccionarios, cada uno de los cuales representa un usuario.

    Ejemplo:
    >>> create_database(5)
    [{'nombre': 'Juan', 'edad': 25}, {'nombre': 'María', 'edad': 30}, {'nombre': 'Pedro', 'edad': 35}, {'nombre': 'Ana', 'edad': 40}, {'nombre': 'Carlos', 'edad': 45}]
    """
    return [
        create_user()
        for _ in range(cant_usuarios)
    ]