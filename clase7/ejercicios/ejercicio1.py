# 1. Ejercicio de List Comprehension con range y for
# Crea un programa que:
# 1. Genere una lista de números del 1 al 10 usando range.
# 2. Cree una nueva lista que contenga el cuadrado de cada número solo si el número es impar.

lista_num = []
for num in range(1, 11):
    lista_num.append(num)
print(lista_num)

cuadrados_impares = [num**2 for num in lista_num if num % 2 != 0]
print(cuadrados_impares)