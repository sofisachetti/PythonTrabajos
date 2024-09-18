# Ejercicio 4: Manipulación de Tuplas y Comprobación de Índices
# • Crea una tupla llamada frutas con los siguientes elementos: ("manzana", "banana", "cereza").
# • Usa el método index para encontrar la posición de la fruta "banana".
# • Verifica si la fruta "naranja" está en la tupla. Si no está, muestra un mensaje indicando que no está presente.

frutas = ("manzana", "banana", "cereza")

posicion_banana = frutas.index("banana")
print(f"La fruta 'banana' se encuentra en la posicion {posicion_banana}.")

valor_a_buscar = input("Ingrese el nombre de la fruta que desea buscar: ")

if valor_a_buscar in frutas:
    print(f"La fruta {valor_a_buscar} está presente en la tupla.")
else:
    print(f"La fruta {valor_a_buscar} no está presente en la tupla.")