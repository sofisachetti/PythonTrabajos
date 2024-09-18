# Ejercicio 2: Contador de Números Específicos
# Escribe un programa que cuente cuántas veces aparece un número
# específico en una lista.
# Instrucciones:
# • Define una lista de números predefinida o pídele al usuario que ingrese los números.
# • Pide al usuario que ingrese un número a buscar.
# • Usa el método count() para determinar cuántas veces aparece el número en la lista.
# • Muestra el resultado.


lista_numeros = [1, 16, 25, 3, 7, 95, 30, 1, 4, 25, 25]
print("Lista de números: ", lista_numeros)

numero_a_buscar = int(input('Ingrese el número que desea buscar: '))

aparicion_de_num = lista_numeros.count(numero_a_buscar)

print(f"El numero {numero_a_buscar} aparece {aparicion_de_num} veces")