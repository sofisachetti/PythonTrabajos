# Ejercicio 2: Verificación de Elementos en una Tupla
# • Crea una tupla llamada mi_tupla con los siguientes elementos: (3, 6, 9, 12, 15).
# • Verifica si el número 6 está en la tupla y muestra un mensaje indicando si está presente o no.
# • Verifica si el número 7 está en la tupla y muestra un mensaje indicando si está presente o no.

mi_tupla = (3, 6, 9, 12, 15)

valor_a_buscar = int(input("Ingrese el valor que desea buscar: "))

if valor_a_buscar in mi_tupla:
    print(f"El numero {valor_a_buscar} está presente en la tupla.")
else:
    print(f"El numero {valor_a_buscar} no está presente en la tupla.")