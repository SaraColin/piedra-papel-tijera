import random
def saludar():
    print("bienvenido al juego de piedra, papel o tijeras")
    nombre_usuario=input("ingresa tu nombre por favor:")
    print(f"muy bien {nombre_usuario}, has tu mejor esfuerzo por ganarme, pero lllo dudo... nadie lo ha hecho")
saludar()

def contar_rontas():
    numero_rondas=input("ccuantasas rondas quires jugar? 1 o 3: ")
    print(f"perfecto, jugaremos {numero_rondas} rondas!!")
contar_rontas()
 
def dar_opciones():
    option=['piedra', 'papel', 'tijerss']
    print(input(f"elige uns de las siguientes opciones: {option}"))
dar_opciones()