# Crear una tupla con varios valores
tupla_mixta = (1, 'Hola', 3.5)

# Mostrar comleta la tupla
print('Tupla completa: ', tupla_mixta)

# Acceder a los elementos de la tupla por su indice (posicion)
print('Primer elemento de la tupla: ', tupla_mixta[0])
print('Segundo elemento de la tupla: ', tupla_mixta[1])
print('Tercer elemento de la tupla: ', tupla_mixta[2])

# Explicacion tuplas inmutables
print('\nLas tuplas no se pueden mmodificar. Intentemos cambiar el primer elemento de la tupla: ')
# TypeError: 'tuple' object does not support item assignment
# Ejemplo de intento de cambio que causaría error
#tupla_mixta[0] = 10

# Explicacion clara de la inmutabilidad
print('Si intentamos hacer "tupla_mixta[0] = 10", Python mostrara error porque no se puede cambiar ningun elemento de una tupla.')

# Mostramos como sí podemos "modificar" una tupla
tupla_mixta = (10, 'Hola', 3.5)
print('\nNueva tupla con el primer elemento cambiado: ', tupla_mixta)
print('Tupla original permanece sin cambios: ', tupla_mixta)