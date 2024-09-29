# 1. Ejercicio de Sets y for
# Crea un programa que reciba una lista de números y realice las siguientes operaciones:
# 1. Crear un set a partir de la lista para eliminar duplicados.
# 2. Iterar sobre el set e imprimir cada número.
# 3. Contar cuántos números son mayores que un valor dado y almacenarlos en un nuevo set.

lista_num = [2, 50, 21, 7, 5, 2, 32, 41, 21]
set_num = set(lista_num)
print(f"Todos los numeros en set sin repetir: {set_num}")

valor_limite = 20
nuevo_set = {i for i in set_num if i < valor_limite}
print(f"Set de numeros menores a 20: {nuevo_set}")

# No funciona
# for i in set_num:
#     valor_limite = 20
#     nuevo_set = {}
#     if i < valor_limite:
#         nuevo_set.add(i)
#         print(f"Set de numeros menores a 20: {nuevo_set}")
