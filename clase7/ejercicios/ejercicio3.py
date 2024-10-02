# 3. Ejercicio de Sets y Operaciones Básicas
# Escribe un programa que:

# 1. Cree dos sets de números.
set_num1 = {15, 2, 46, 51, 37, 12, 8}
set_num2 = {6, 27, 15, 3, 8, 2}

# 2. Realice operaciones de unión, intersección y diferencia entre estos sets.
# 3. Imprima los resultados de cada operación.

union = set_num1 | set_num2
print(f"Todos los numeros {union}")

interseccion = set_num1 & set_num2
print(f"La interseccion de los numeros: {interseccion}")

diferencia = set_num1 - set_num2
print(f"La diferencia entre los numeros: {diferencia}")