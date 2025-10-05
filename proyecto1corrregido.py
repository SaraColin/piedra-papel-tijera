import random
def saludar_usuario():
    print("bienvenido al juego de piedra, papel o tijera")
    nombre=input(" ¿cual es tu nombre?:") 
    print(f"hola {nombre}, tendras que escoger una de las siguientes opciones  e intentar ganarme. intentalo, tal vez corras con suerte... ")
saludar_usuario()
def seleccionar_rondas():
    while True:
        respuesta = input("¿Quieres jugar 1 o 3 rondas? Escribe el número: ")

        if respuesta == '1' or respuesta == '3':
            rondas = int(respuesta)
            return rondas
        else:
            print("Error: Opción inválida. Por favor, escribe solo '1' o '3'.")


numero_de_rondas = seleccionar_rondas()



def dar_opciones():
    opciones=["piedra", "papel", "tijera"]
    print(input(f"tienes que elegir una de las siguientes opciones: {opciones}"))
dar_opciones()
#correccion de estas funciones pendiente
