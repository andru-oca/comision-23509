# nombre:str = input("ingresa tu nombre:\n")

# print("Hola, " + nombre)


# CREAR UN FORMULARIO USUARIO CARGA


nombre = input(" ingrese su nombre: \n")
apellido = input(" ingrese su apellido: \n")
correo = input(" ingrese su correo: \n")
password = input(" ingrese su password: \n")



text_salida = f"""
    Hola soy : {nombre}, {apellido}
    Mi email es : {correo:_^20}
    Y el password es : {password}
"""


print(text_salida)

with open(f"{nombre}_user.txt","w",encoding="utf8") as file:
    file.write(text_salida)




