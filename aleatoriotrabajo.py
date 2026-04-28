# import random

# jugadores = ["Persona 1", "Persona 2", "Persona 3"]
# distancias = {jugador: random.randint(60, 190) for jugador in jugadores}

# # 1. Mostramos los resultados
# for jugador, golpe in distancias.items():
#     print(f"{jugador} golpeó la bola a {golpe} metros.")

# # 2. Encontramos cuál fue la distancia máxima
# record = max(distancias.values())

# # 3. Buscamos a todos los que alcanzaron esa distancia (por si hay más de uno)
# ganadores = [nombre for nombre, golpe in distancias.items() if golpe == record]

# print("-" * 34)
# if len(ganadores) > 1:
#     print(f"¡Empate! Los ganadores con {record} metros son: {', '.join(ganadores)}")
# else:
#     print(f"El ganador es {ganadores[0]} con {record} metros.")


import random

# Configuración inicial
# jugadores = ["Jugador 1", "Jugador 2", "Jugador 3", "Jugador 4"]
# posiciones = [0, 0, 0, 0]
# meta = 50
# turno = 0

# print("--- LUDO ---")

# while max(posiciones) < meta:
#     nombre = jugadores[turno]
    
#     # Lanzamiento automático
#     dado = random.randint(1, 6)
#     posiciones[turno] += dado
    
#     print(f"{nombre} sacó {dado}  | Total: {posiciones[turno]}")

#     # Si alguien gana, salimos del bucle 
#     if posiciones[turno] >= meta:
#         print("-" * 30)
#         print(f"¡{nombre} GANÓ EL JUEGO!")
#         break

#     # Cambio de turno (del 3 vuelve al 0)
#     turno = (turno + 1) % 4