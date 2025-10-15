import random

def saludar_usuario():
   print("hola, bienvenido al juego de piedra papel o tijeras")
   nombres=input("ingresa tu nombre por favor:")
   print(f"perfecto {nombres}!!, ahora tendrás que seleccionar uno de los siguienets opciones, pero antes...")
saludar_usuario()


def seleccionar_rundas():
    """
    Pregunta al usuario si quiere jugar 1 o 3 rondas, valida la entrada
    y devuelve el número de rondas como un entero.
    """
    while True:
        respuesta = input("¿Cuántas rondas quieres jugar, 1 o 3? ")
        if respuesta == '1' or respuesta == '3':
            resultado = int(respuesta)
            return resultado
        else:
            print("Por favor, vuelve a intentarlo, solo puedes elegir 1 o 3 como opción.")

def jugar():
    
    #Llamamos a tu función para saber cuántas rondas jugar.
    rondas_totales = seleccionar_rundas()
    
    print(f"Jugaremos {rondas_totales}")
    
    # Creamos un bucle que se repite el número de veces elegido.
    # Usamos 'range(1, rondas_totales + 1)' para que cuente desde 1 (Ronda 1, Ronda 2...)
    for ronda_actual in range(1, rondas_totales + 1):
        print(f"\nEmpezando Ronda {ronda_actual} de {rondas_totales}")
        


    # PASO 4: Este mensaje se muestra cuando el bucle 'for' ha terminado.
    print("\n¡Juego terminado! Gracias por jugar.")

# --- Iniciar el juego ---
# Esta línea llama a la función principal para que todo comience.
jugar()

 

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


