# Desempaquetadoo basico de tuplas
#Crear una tupla con varios tipos de datos
mi_tupla = (1, 'python', 3.14)
# Desempaquetar la tupla
numero, lenguaje, pi = mi_tupla
# Mostrar el valor de cada variable despues del desempaquetado
print('Numero: ', numero)
print('Lenguaje: ', lenguaje)
print('Valor de Pi: ', pi)

# Ejemplo 2: Numero de variables no coincide con el num de elementos
# Crear una tupla con tres elementos
mi_tupla = (1, 'python', 3.14)
#Intentar desempaquetar en dos variables (esto causa error)
#numero, lenguaje = mi_tupla

# Ejemplo 3: Desempaquetado con el operador +
mi_tupla = (1, 'python', 3.14, 'Tuplas', 'Desempaquetado')
#Desempaquetar la tupla con el operador * para capturar varios elementos
primer_elemento, *resto = mi_tupla
#Mostrar los resultados
print('\nPrimer Elemento: ', primer_elemento)
print('Resto de los elementos: ', resto)
