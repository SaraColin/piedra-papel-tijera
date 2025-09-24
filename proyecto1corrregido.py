import random

# --- BIENVENIDA E INSTRUCCIONES INICIALES ---
saludo1 = ("¡Bienvenido al juego!")
saludo2 = ("Prepárate para jugar piedra, papel o tijera...")
saludo3 = ("Suerte, y que gane el mejor")
print(saludo1)
print(saludo2)
print(saludo3)

nombre = input("\n¿Cuál es tu nombre?: ")
print(f"¡Hola, {nombre}! Vamos a comenzar el juego 🪨📄✂️")

# --- SELECCIÓN DE RONDAS ---
rondas = 0
while rondas not in [1, 3]:
    try:
        rondas = int(input("¿Quieres jugar 1 o 3 rondas?: "))
        if rondas not in [1, 3]:
            print("Por favor, elige solo 1 o 3.")
    except ValueError:
        print("Eso no es un número. Intenta de nuevo.")


# --- PREPARACIÓN DEL JUEGO ---
opciones_validas = ["piedra", "papel", "tijera"]
puntos_jugador = 0
puntos_compu = 0
empates = 0


# --- CICLO PRINCIPAL DEL JUEGO ---
for numero_ronda in range(1, rondas + 1):
    print(f"\n--- Ronda {numero_ronda} de {rondas} ---")
    
    # Elección del jugador con validación
    eleccion_jugador = input("Elige una opción: piedra, papel o tijera\n").lower()
    while eleccion_jugador not in opciones_validas:
        print("Opción inválida. Intenta de nuevo.")
        eleccion_jugador = input("Elige piedra, papel o tijera\n").lower()
    
    # Elección de la computadora
    eleccion_compu = random.choice(opciones_validas)
    print(f"La computadora eligió: {eleccion_compu}")
    
    # Determinar el resultado de la ronda
    if eleccion_jugador == eleccion_compu:
        print("¡Empate en esta ronda!")
        empates += 1
    elif (
        (eleccion_jugador == "piedra" and eleccion_compu == "tijera") or
        (eleccion_jugador == "papel" and eleccion_compu == "piedra") or
        (eleccion_jugador == "tijera" and eleccion_compu == "papel")
    ):
        print(f"¡Ganaste esta ronda, {nombre}!")
        puntos_jugador += 1
    else:
        print(f"Perdiste esta ronda, {nombre}...")
        puntos_compu += 1

# --- RESULTADO FINAL DEL JUEGO ---
print("\n--- ¡Fin del juego! ---")
print(f"Puntuación final:")
print(f"Puntos de {nombre}: {puntos_jugador}")
print(f"Puntos de la computadora: {puntos_compu}")
print(f"Empates: {empates}")

if puntos_jugador > puntos_compu:
    print(f"\n¡Felicidades, {nombre}! ¡Ganaste el juego! 🎉")
elif puntos_jugador < puntos_compu:
    print(f"\nLo siento, {nombre}, perdiste el juego... 😢")
else:
    print("\n¡El juego terminó en empate! 🤝")