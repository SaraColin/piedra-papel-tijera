import random
def saludar_usuario():
    print("bienvenido al juego de piedra, papel o tijera")
    nombre=input(" ¿cual es tu nombre?:") 
    print  (f"hola {nombre}, tendras que escoger una de las siguientes opciones  e intentar ganarme. intentalo, tal vez corras con suerte... ")
saludar_usuario()
def seleccionar_rundas():#repasar
    while True:
        respuesta=input("¿cuantas rondas quieres jugar, 1 o 3? escribe tu respuesta:")
        
        if respuesta=='1' or respuesta=='3':
            resultado=int(respuesta)
            return resultado
        else:
            print("debes de elegir solo la opcion 1 o 3")
seleccionar_rundas()

def dar_opciones():
    opciones=["piedra", "papel", "tijera"]
    print(input(f"tienes que elegir una de las siguientes opciones: {opciones}"))

    
    print(f"la computadora  elegio {eleccion}")
    eleccion=opciones
    
    eleccion=random.choice(opciones)
dar_opciones()

