# Definir una matriz de 3x3

matriz = [
    [1, 2, 3], # Fila 0    // Cada fila se separa con una coma
    [4, 5, 6], # Fila 1
    [7, 8, 9]  # Fila 2
]

# Acceder y mostrar algunos elementos especificos de la matriz
print('Algunos elementos de la matriz: ')
print('Elementos en la fila 0, columna 0: ', matriz[0][0])
print('Elemento en la fila 1, coulmna 2: ', matriz[1][2])

# Modificar elementos especificos de la matriz
print('\n Modificando elementos específicos: ')
matriz[0][1] = 10 #Le asignamos una nuevo valor, cambia el elemnto en la fila 0 columna 1 a valor 10
matriz[2][0] = 15
print('Matriz después de las modificaciones: ')
print(matriz) # Imprime [[1, 10, 3], [4, 5, 6], [15, 8, 9]]

# Acceder a una fila completa
print('\n Accediendo a una fila completa: ')
fila_completa = matriz[1] #Obtener toda la fila
print('Fila completa en la posición 1: ', fila_completa)

# Reemplazar una fila completa
print('\nReemplazando una fila completa: ')
matriz[1] = [20, 21, 22]
print('Matriz después de reemplazar la fila 1: ', matriz)

# Trabajar con una submatriz (parte de una matriz)
submatriz = [matriz[0][1:3], matriz[1][1:3]] # Extraer submatriz de las columnas 1 a 2 de las filas 0 y 1
print('\nSubmatriz extraída: ', submatriz)

# Mostramos toda la matriz al final
print('\nMatriz completa al final: ')
print(matriz[0])
print(matriz[1])
print(matriz[2])
