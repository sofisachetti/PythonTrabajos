# 4. Ejercicio de while con Condiciones y Contadores
# Desarrolla un programa que:
# 1. Use un bucle while para generar números de la serie de Fibonacci.
# 2. Continúe generando números hasta que el número actual sea mayor
# o igual a 100.
# 3. Imprima la serie de Fibonacci generada.

a = 0
b = 1

while True:
    a += b
    b += a
    
    if b >= 100:
        break
    print(a,b)