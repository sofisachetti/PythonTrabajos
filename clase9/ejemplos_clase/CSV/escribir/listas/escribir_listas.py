import csv

# definir nombres columnas
fieldnames = ['nombre', 'edad', 'ciudad']

#newline='' se utiliza para evitar lineas en blanco adicionales en algunos sistemas operativos
with open('archivo.csv', 'w', newline='') as file:
    #cramos un objeto DicWriter. Se pasa el archivo y la lista de nombres de columnas(fieldnames)
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    
    #escribir la fila de encabezados en el archivo csv
    #esto crea la primera fila con los nombres de columnas
    writer.writeheader()
    
    #escribir una fila con los datos de un archivo csv
    #cada diccionario debe tener claves que coincidan con los nombres de las columnas
    writer.writerow({'nombre' : 'Ana', 'edad' : '35', 'ciudad' : 'Neuquen'})
    
    #escribir multiples filas de datos en el archivo csv
    writer.writerows([
        {'nombre' : 'Julia', 'edad' : '35', 'ciudad' : 'Neuquen'},
        {'nombre' : 'Mario', 'edad' : '35', 'ciudad' : 'Neuquen'}
    ])