productos = [
    {'nombre' : 'leche', 'precio' : 1200, 'cantidad en stock' : 15},
    {'nombre' : 'huevos', 'precio' : 800, 'cantidad en stock' : 6},
    {'nombre' : 'yerba', 'precio' : 2100, 'cantidad en stock' : 4},
    {'nombre' : 'cafe', 'precio' : 2600, 'cantidad en stock' : 10},
]

producto = productos[1]
nombre_producto = producto.get('nombre')
precio_producto = producto.get('precio')

print(f"El producto {nombre_producto} cuesta ${precio_producto}")