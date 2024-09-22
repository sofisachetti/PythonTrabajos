# Ejercicio 1: Lista de Compras
# Crea un programa que gestione una lista de compras. El programa debe permitir añadir artículos a la lista y eliminar el último artículo si el usuario se arrepiente.
# Instrucciones:
# • Define una lista vacía para la lista de compras.
# • Usa un bucle para pedir al usuario que ingrese artículos.
# • Agrega cada artículo a la lista usando append().
# • Permite al usuario eliminar el último artículo usando pop() si así lo desea.
# • Muestra la lista final de compras.

lista_compras=[]

while True:
    # Pide al usuario los articulos
    articulos = input("Ingrese un articulo para la lista de compras ('done' para finalizar): ")
    # Si no quiere cargar mas a la lista, con 'done' se cierra el bucle
    if articulos == 'done':
      break
    # Agregamos los alementos a la lista de compras
    lista_compras.append(articulos)
    
# Le consultamos al usuario si quiere eliminar el ultimo articulo que ingreso
eliminar_ultimo = input("¿Desea eliminar el ultimo articulo de la lista? si/no: ")
if eliminar_ultimo == 'si':
  lista_compras.pop()
  print("Se ha eliminado el ultimo elemento de la lista.")
  print(f"La lista final es: {lista_compras}")
else:
  print(f"La lista final es: {lista_compras}")