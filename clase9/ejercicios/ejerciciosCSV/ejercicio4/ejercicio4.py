# Ejercicio 4: Leer un archivo CSV
# Crea un programa que lea los datos de un archivo CSV datos.csv y
# muestre cada fila en la consola.

import csv

with open('datos.csv', 'r') as file:
    reader = csv.reader(file)
    for fila in reader:
        print(fila)