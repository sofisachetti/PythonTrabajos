# Ejercicio 2: Generador de Números Aleatorios con el Módulo random
# • Objetivo: Trabajar con funciones de generación de números
# aleatorios del módulo random.
# • Descripción: Simula el lanzamiento de un dado y genera una lista de números aleatorios.
# • Instrucciones:
# ✓ Simula el lanzamiento de un dado de 6 caras (números del 1 al 6) cinco veces.
# ✓ Genera una lista de 10 números aleatorios entre 1 y 100.
# ✓ Selecciona aleatoriamente un número de la lista generada.

import random

for dado in range(1,6):
    print(f"El dado cayo en {random.randint(1,6)}")

num_aleatorios = []
for num in range(10):
    num_aleatorios.append(random.randint(1, 100))
    print(f"Los numeros aleatorios son {num_aleatorios}")

num_aleatorio = random.choice(num_aleatorios)
print(f"Numero elegido: {num_aleatorio}")