# Ejercicio 8: Modificar un Valor en un Diccionario Anidado
# 1. Crea un diccionario que contenga información sobre una tienda de libros, con las siguientes claves:
# o nombre_tienda
# o libros, que es una lista de diccionarios, donde cada diccionario
# representa un libro con claves titulo y precio.
# 2. Cambia el precio del segundo libro en la lista a un nuevo valor (por ejemplo, 15.99).
# 3. Imprime el título y el precio del segundo libro después de la modificación.

tienda_libros = {
    'nombre': 'Cuspide',
    'libros' : [
        {'titulo': 'Orgullo y Prejuicio', 'precio': 20500},
        {'titulo': 'Cien Anios de Soledad', 'precio': 25500},
        {'titulo': 'Mujercitas', 'precio': 15900},
        {'titulo': 'Rayuela', 'precio': 22300},
        {'titulo': 'La Casa de los Espiritus', 'precio': 19900}
    ]
}

tienda_libros['libros'][1]['precio'] = 26000
titulo_segundo_libro = tienda_libros['libros'][1]['titulo']
precio_segundo_libro = tienda_libros['libros'][1]['precio']
print(f"El segundo libro es: {titulo_segundo_libro}, y su precio actualizado es: {precio_segundo_libro}")