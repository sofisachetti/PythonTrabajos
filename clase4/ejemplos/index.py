# Crear una tupla con varios elementos
mi_tupla = (10, 20, 30, 40, 50)

# Ecnontrar la posicion del numero 30 en la tupla
indice_de_30 = mi_tupla.index(30)
print('El numero 30 se encuentra en la posicion ', indice_de_30, ' de la tupla.')

# Verificar si un valor esta en tupla antes de buscar su indice
valor_buscado = 60

if valor_buscado in mi_tupla:
    # si el valor esta en la tupla, encontrar su indice
    indice_del_valor = mi_tupla.index(valor_buscado)
    print(f"El numeor {valor_buscado} se encuentra en la posicion {indice_del_valor} de la tupla.")
else: # si el valor no está en la tupla, mostrar un mensaje
    print(f"El numero {valor_buscado} no está en la tupla.")