# Ejercicio 3: Suma de Sublistas
# Crea un programa que tome una lista de números y calcule la suma de una sublista especificada por el usuario.
# Instrucciones:
# • Define una lista de números predefinida.
# • Pide al usuario que ingrese el índice de inicio y el índice de fin para la sublista.
# • Usa slicing para obtener la sublista.
# • Suma los elementos de la sublista.
# • Muestra la suma.

lista_numeros = [1, 16, 25, 3, 7, 95, 30, 1, 4, 25, 25]
print('Lista de números: ', lista_numeros)

inicio = int(input("Ingrese el índice de inicio de la sublista: "))
fin = int(input("Ingrese el índice de fin de la sublista: "))

sublista = lista_numeros[inicio:fin]
print("La sublista es: ", sublista)

suma = sum(sublista)
print("La suma de la sublista es: ", suma)