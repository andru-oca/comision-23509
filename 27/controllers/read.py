def read_user(dni:str,db:list[dict]=None)->(dict|None):
    """
    Busca un usuario en la base de datos (db) mediante su número de identificación (dni).

    Parameters:
    - dni (str): El número de identificación del usuario que se busca en la base de datos.
    - db (list[dict], optional): La base de datos de usuarios. Si no se proporciona, se imprime un mensaje y la función devuelve None.

    Returns:
    dict or None: Un diccionario que representa al usuario encontrado o None si la base de datos no está disponible o el usuario no está en la base de datos.

    Example:
    >>> database = [
    ...     {"dni": "123456789", "nombre": "Erik", "edad": 28, "email": "erik@example.com"},
    ...     {"dni": "987654321", "nombre": "Ingrid", "edad": 25, "email": "ingrid@example.com"}
    ... ]
    >>> read_user("123456789", database)
    Usuario encontrado:
    dni: 123456789
    nombre: Erik
    edad: 28 años
    email: erik@example.com
    
    {'dni': '123456789', 'nombre': 'Erik', 'edad': 28, 'email': 'erik@example.com'}
    """
        
    if db is None:
        print("che, noru, no me pasaste una db")
        return None
    
    _user = {}

    for user in db:
        if user["dni"] == dni:
            print(f"""
                Usuario encontrado:
                dni: {user["dni"]}
                nombre: {user["nombre"]}
                edad: {user["edad"]} años
                email: {user["email"]}
            """)
            _user = user
            
    if len(_user) == 0:
        print("No hay usuario, recomiendo crear uno")
    return _user

