# 3. Ejercicio con range, enumerate, y break/continue
# Escribe un programa que:
# 1. Itere sobre una lista de cadenas usando enumerate para mostrar el índice y el valor.
# 2. Utilice continue para saltar cadenas vacías.
# 3. Utilice break para detener la iteración si se encuentra una cadena con más de 5 caracteres.

lista_cadenas = ["Hola", "", "estoy", "", "aprendiendo", "Python", ""]

for indice, cadena in enumerate(lista_cadenas):
    if cadena == "":
        continue
    if len(cadena) > 5:
        print(f"'{cadena}' contiene mas de 5 caracteres.")
        break
    print(f"Indice cadena: {indice}, Cadena: {cadena}")