# Ejercicio 1: Operaciones Básicas con Tuplas
# • Crea una tupla llamada mi_tupla con los siguientes elementos: (5, 10, 15, 20, 25).
# • Usa el método count para contar cuántas veces aparece el número 10 en la tupla.
# • Usa el método index para encontrar la posición del número 20 en la tupla.
# • Muestra los resultados de las operaciones anteriores.

mi_tupla = (5, 10, 15, 20, 25)

buscar = mi_tupla.count(10)
print(f"Cantidad de veces que se repite el número 10 dentro de la tupla: {buscar}")

posicion = mi_tupla.index(20)
print(f"El número 20 se encuentra en la posición {posicion} dentro de la tupla.")