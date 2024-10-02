# 6. Ejercicio de List Comprehension y range
# Crea un programa que:
# 1. Use range para generar una lista de números del 1 al 15.
# 2. Utilice list comprehension para crear una nueva lista con el cubo
# de los números pares.

numeros = list(range(1, 16))

cubos_pares = [num**2 for num in numeros if num % 2 == 0]
print(cubos_pares)