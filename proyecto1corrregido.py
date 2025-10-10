import random
def saludar_usuario():
    print("bienvenido al juego de piedra, papel o tijera")
    nombre=input(" ¿cual es tu nombre?:") 
    print  (f"hola {nombre}, tendras que escoger una de las siguientes opciones  e intentar ganarme. intentalo, tal vez corras con suerte... ")
saludar_usuario()
def seleccionar_rundas():#hacer que tenga la funcion de jugar tres partidas
    while True:
        respuesta=input("¿cuantas rondas quieres jugar, 1 o 3?")
        if respuesta=='1' or respuesta=='3':
            resultado=int(respuesta)
            return resultado
        else :
            print("por favor, soslo elije 1 o 3")
seleccionar_rundas()

def dar_opciones():#repasar
    opciones=["piedra", "papel", "tijera"]
    eleccion_jugador=input(f"tienes que elegir una de las siguientes opciones: {opciones}")
    eleccion_compu=random.choice(opciones)
    print(f"Tú elegiste: {eleccion_jugador}")
    print(f"La computadora eligió: {eleccion_compu}")
    
    if eleccion_jugador==eleccion_compu:#volver a hacerlo
        print("es un empate!!!")
    elif (eleccion_jugador == "piedra" and eleccion_compu == "tijera") or \
        (eleccion_jugador == "tijera" and eleccion_compu == "papel") or \
        (eleccion_jugador == "papel" and eleccion_compu == "piedra"):
        print("¡Ganaste!")
    else:
        print("¡Perdiste!")
        
dar_opciones()


