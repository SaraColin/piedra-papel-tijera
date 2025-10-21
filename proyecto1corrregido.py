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

#termin\ar funciones, vover a hacer toda la logica en 20 minutos maximo


