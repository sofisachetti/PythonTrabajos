# Solicita al usuario que ingrese un número decimal.
# Usa las siguientes funciones del módulo math para realizar diferentes cálculos:
# ✓ math.ceil(): Redondear al entero superior.
# ✓ math.floor(): Redondear al entero inferior.
# ✓ math.sqrt(): Obtener la raíz cuadrada.
# ✓ math.factorial(): Calcular el factorial (solo si es un número entero no negativo).
# ✓ math.pow(): Elevar el número a la potencia de otro número.

import math

numero_usuario = float(input("Ingrese un numero decimal: "))

numero_ceil = math.ceil(numero_usuario)
print(f"El numero {numero_usuario} redondeado hacia arriba es: {numero_ceil}")

numero_floor = math.floor(numero_usuario)
print(f"El numero {numero_usuario} redondeado hacia abajo es: {numero_floor}")

numero_sqrt = math.sqrt(numero_usuario)
print(f"La raiz cuadrada del numero {numero_usuario} es: {numero_sqrt}")

numero_factorial = math.factorial(numero_ceil)
print(f"El factorial del numero {numero_usuario} (redondeado hacia arriba) es: {numero_factorial}")

numero_pow = math.pow(numero_usuario, 3)
print(f"La potencia del numero {numero_usuario} es: {numero_pow}")
