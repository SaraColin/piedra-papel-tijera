import random
def saludar():
    print("bienvenido al juego de piedra, papel o tijeras")
    nombre_usuario=input("ingresa tu nombre por favor:")
    print(f"muy bien {nombre_usuario}, has tu mejor esfuerzo por ganarme, pero lo dudo... nadie lo ha hecho")
saludar()

def contar_rontas():
    numero_rondas=input("cuantas rondas quires jugar? 1 o 3: ")
    print(f"perfecto, jugaremos{numero_rondas} rondas.")
contar_rontas()
 
def dar_opciones():
    opciones=['piedra', 'papel', 'tijerss']
    print(input(f"elige una de las siguientes opciones: {opciones}"))
dar_opciones()

def contar_puntos():
     if puntos_compu==1
        print("compu ha perdido")