# saludo:str = 'hola mundo'
# print(saludo)

# ------------------ ARRAYS | LIST
"""
fruit_emojis:list = [
    "apple: 🍎",
    "banana: 🍌",
    "orange: 🍊",
    "watermelon: 🍉",
    "grape: 🍇",
    "strawberry: 🍓",
    "pizza: 🍕" ,
    "cherry: 🍒",
    "peach: 🍑",
    "pear: 🍐",
    "pineapple: 🍍",
    "mango: 🥭",
    "kiwi: 🥝",
    "avocado: 🥑",
    "raspberry: 🍓",
    "blackberry: 🍇",
    "coconut: 🥥",
    "lemon: 🍋",
    "lime: 🍈",
    "tangerine: 🍊",
]


##  --> ~ push ->  append

fruit_emojis.append("pizza: 🍕")
fruit_emojis.append("pizza: 🍕")
# fruit_emojis.append(["Marcelo",True])
# fruit_emojis.append( lambda x:x )


# ----> pop
fruit_emojis[0] , fruit_emojis[-1]  = fruit_emojis[-1] , fruit_emojis[0] 
uva:str = fruit_emojis.pop(4)
fruit_emojis.remove("pizza: 🍕")


# ---> INSERT
fruit_emojis.insert(4,uva+" -> 🍷")

print("==> SIN LAMBDA y sin uvas\n", fruit_emojis)


#index = 1
for index,fruta in enumerate(fruit_emojis,start=100):
    print(f"{index:3} : {fruta}")
#   index += 1


# -- > 

print("-"*50)
# for index,fruit in enumerate(fruit_emojis):
#     if "🍕" in fruit:
#         fruit_emojis.pop(index)

# print( fruit_emojis )

# list comprehension 

frutas_sin_pizza:list = [
    fruta                       # variable a rellenar en esta lista
    for fruta in fruit_emojis   # iteracion con la variable declarada
    if "🍕" not in fruta        # condicion que debe cumplir
]


print(frutas_sin_pizza)


print("-"*50)

five_frutas:list = fruit_emojis[:5]
resto_frutas:list = fruit_emojis[5:]

print("-"*50)
# print(five_frutas)
print("-"*50)
# print(resto_frutas)


print("-"*50)

# Fede 

stock_frutas:list = resto_frutas +["pie : 🎂"]*10 + five_frutas * 5
# print(stock_frutas)

print("-"*50)


# SET
frutas_unicas:set = set( stock_frutas )

print(frutas_unicas)

conteo_frutas:list = []

for u in frutas_unicas:
    counter = 0
    
    for fruta in stock_frutas:
        if u == fruta:
            counter += 1
    
    conteo_frutas.append([u,counter])

print(conteo_frutas)


# INMUTABLES

print("-"*50)

verduleria:tuple = ("doña petrona" , True , [])

for fruta in stock_frutas:
    verduleria[-1].append(fruta)


print(verduleria)

"""
# DESAFIO 
"""

* Escribe un programa que muestre por consola (con un print) los
* números de 1 a 100 (ambos incluidos y con un salto de línea entre
* cada impresión), sustituyendo los siguientes:
* - Múltiplos de 3 por la palabra "fizz".
* - Múltiplos de 5 por la palabra "buzz".
* - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".

"""

# dict


flavia:dict = {
    "nombre" : "Flavia" ,
    "email":  "flav@mail.com",
    "password" : "lkjaskldjlaksd",
    10 : "traeme la copa messi",
    ("flavia","1234") : 1_000_000
}


for k,v in flavia.items():
    print(f"{k} ==> {v}")


# print(flavia["email"])

# user:str = input("ingrese el usuario\n")
# pwd:str  = input("ingrese el pass\n")

# print(flavia.get((user,pwd),"algo está mal"))

# ---------  

import random
import string


users:list = "carolina,dario,santiago,pablo".split(",")
passwords:list = [  
    ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
    for _ in range(4)   ]

print(users,passwords)


lista_users:list = [
    {
        "nombre":user,
        "email" : f"{user}_codo@mail.com",
        "password": pwd,
        "status" :True
    }
    for user , pwd in zip(users,passwords)
]


print(lista_users)

for usuario_creado in lista_users:
    usuario_text:str = f"""
    Bienvenido, {usuario_creado["nombre"]} a codo a codo!
    Tu email: {usuario_creado["email"]}
    Password provisorio: {usuario_creado["password"]}

    Gracias por unirte!
    """
    with open(f'{usuario_creado["nombre"]}.txt',"w",encoding="utf8")as f:
        f.write(usuario_text)






