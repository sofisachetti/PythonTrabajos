# Ejercicio 5: Escribir en un archivo CSV
# Crea un programa que guarde los siguientes datos en un archivo CSV
# alumnos.csv: ["Nombre", "Edad"], ["Ana", 23], ["Luis", 25].

import csv

datos = ['nombre', 'edad']

with open('alumnos.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=datos)
    writer.writeheader()
    
    writer.writerows([
        {'nombre': 'Ana', 'edad': 23},
        {'nombre': 'Luis', 'edad': 25}
    ])