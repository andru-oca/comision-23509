"""
    esto es un comentario en bloque

    - condicionales
    - importacion modulos
    - iteradores for y while
    - texto
    - sqlite3 => como insertar usuarios
    - año bisiesto => guardar

"""

# if else elif 

# SISTEMA DE LOGIN 

from modulo.db import PASSWORD , USER


# username = input("ingrese su username:\n")

# if username == USER:
#     pwd  = input("ingrese su pwd :\n")

#     if pwd == '':
#         print("contraseña está vacia 😨")
#     elif ' ' in pwd:
#         print("la constraseña no puede tener espacios vacios")
#     elif pwd.isdigit():
#         print("guarda que solo estás usando datos numericos")
#     else:
#         if pwd != PASSWORD:
#             print("No es válido 😡")
#         else:
#             print(f"Bienvenido {username}")


# else:
#     print("usuario no encontrado")

# ITERADORES

# flag:bool = True
# retries = 3
# PASSWORD = "123A"


# while flag:
    
#     pwd = input("ingrese contraseña:\n")

#     if (pwd == PASSWORD) and (retries != 0):
#         flag = not flag

#     elif retries == 1:
#         print("Salga y vuelva a intentar")
#         break

#     else:
#         retries -= 1 
#         print(f"""
#         Password no válido, cantidad de intentos
#         restantes : 
#             {retries}
#         """)
# else:
#     print("El ciclo ha concluido")


# ITERACION

texto = "hola mundo desde codo a codo"

# for i in range( len(texto) ):
#     print(texto[i])


# for char in texto:
#     print(char)

# EJERCICIO #1 
# CREAR UN SOFT QUE ME PERMITA SABER 
# LA CANTIDAD DE AÑOS BISIESTOS EXISTE DESDE
# UNA FECHA DE INICIO Y UNA FECHA DE FIN



# print(f"""
#     {'Leap year software':~^30}
# """
# )

# inicio = input(f"{'Ingrese el primer año':~^30}\n")
# fin = input(f"{'Ingrese el año final':~^30}\n")

# counter = 0

# if inicio.isdigit() and fin.isdigit():
#     inicio , fin = int(inicio) , int(fin)

#     for year in range(inicio,fin,1):
#         primera_logica = year % 400 == 0
#         segunda_logica = (year % 4 == 0) and (year % 100 != 0)

#         if primera_logica or segunda_logica:
#             counter += 1
#             print(f"El año: {year} es bisiesto 😀")

#     else:
#         print(f"La cantidad de años bisiestos es : {counter}")


#     print(f"""
#         {'Gracias por usarnos':~^30}
#     """
#     )

# else:
#     print("Que pusiste zapallo?")



## --

import sqlite3
db_nombre = 'libreria_23509'

conn = sqlite3.connect(db_nombre + ".db")

cursor = conn.cursor()


ddl_table = f"""
    CREATE TABLE USER 
    (
            id_user INT PRIMARY KEY
        ,   nombre VARCHAR
        ,   password VARCHAR
    )
"""
cursor.execute(ddl_table)
conn.commit()

flag:bool = True
chars_ruptura =  ['','n','N','no','No','NO']
id_counter = 1
input_option = 's'

while flag :


    
    if input_option in chars_ruptura:
        flag = not flag
    else:

        username= input("ingrese su username: \n")
        password= input("ingrese su password: \n")

        insert_query = f"""
        INSERT INTO USER
        VALUES
        ( {id_counter},'{username}','{password}' )
        """
        id_counter += 1
        cursor.execute(insert_query)
        print(f"USUARIO: {username} ha sido creado")

    input_option = input("Desea seguir insertado usuarios :\n")

else:
    print("Se comitean los cambios y se cierra la base de datos")
    conn.commit()
    conn.close()












