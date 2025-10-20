import random

def seleccionar_rundas():
  
    while True:
        respuesta = input("¿Cuántas rondas quieres jugar, 1 o 3? ")
        if respuesta == '1' or respuesta == '3':
            resultado = int(respuesta)
            return resultado
        else:
            print("Por favor, vuelve a intentarlo, solo puedes elegir 1 o 3 como opción.")
#se elimin[o la funcion de poder jugar con mas de una partida, asi que tengo que hacer una nueva y que si funcione]

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


