# Calcular precio final de un producto con descuento del 15% si el precio inicial es mayor a 200

precio = float(input("Ingrese el valor del producto: "))

if precio > 200:
    descuento = (precio * 15) / 100
    precio_final = precio - descuento
    print(f"Tiene un descuento del 15%. El precio final del producto es de: ${precio_final}.")
else:
    print(f"Este producto no tiene descuento.")