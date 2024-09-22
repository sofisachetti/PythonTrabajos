# Definimos una lista
mi_lista = ['a', 'b', 'c', 'd', 'e']

# Acceso a la sublista (slicing)
print("Sublista (indice 1 a indice 3): ", mi_lista[1:4])
print("Sublista (inicia a 3): ", mi_lista[:3])
print("Sublista (indice 2 al final): ", mi_lista[2:])
print("_______________________________________________")
# Acceso con paso en slicing
print("Sublista con paso 2: ", mi_lista[::2]) # devuelve a, c,e / salta de a uno, ind 0, salta el 1, pasa al 2, el 3 lo salata y pasa al 4
print("Sublista con paso 2 en rango (1 a 4): ", mi_lista[1:4:2])

# Iteracion a traves d una lista
print("Iteracion a traves de la lista: ")
for elemento in mi_lista:
    print(elemento)