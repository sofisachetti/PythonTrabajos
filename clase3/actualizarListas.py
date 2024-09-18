# Lista inicial
mi_lista = [10, 20, 30, 40, 50]
print('Lista original: ', mi_lista)

# Actualizar un elemento en específico
mi_lista[2] = 35 #Le asignamos nuevo valor desde el indice
print('Lista después de actualizar el 3er elemento: ', mi_lista)

# Actualizar un elemento con indice negativo
mi_lista[-1] = 60
print('Lista despues de actualizar el último elemento: ', mi_lista)

# Actualizar varios elementos utilizando slicing
mi_lista[1:4] = [25, 35, 45]
print('Lista despues de actualizar un rango de elementos: ', mi_lista)

# Actualizar basado en una condicion
for i in range(len(mi_lista)):
    if mi_lista[i] > 30:
        mi_lista[i] += 10
print('Lista despues de actualizar elementos mayoresque 30: ', mi_lista)