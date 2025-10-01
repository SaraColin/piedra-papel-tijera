import random
def saludar_usuario():
    print("bienvenido al juego de piedra, papel o tijera")
    nombre=input(" ¿cual es tu nombre?:") 
    print(f"hola {nombre}, tendras que escoger una de las siguientes opciones  e intentar ganarme. intentalo, tal vez corras con suerte... ")
saludar_usuario()

def dar_opciones():
    opciones=["piedra", "papel", "tijera"]
    print(input(f"tienes que elegir una de las siguientes opciones: {opciones}"))
dar_opciones()


