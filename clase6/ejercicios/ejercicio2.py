# 2. Ejercicio de while y for
# Desarrolla un programa que haga lo siguiente:
# 1. Usar un bucle while para pedir al usuario que ingrese números hasta que se ingrese el número 0.
# 2. Usar un bucle for para calcular la suma de los números ingresados, excluyendo el 0.

numeros_ingresados = []

while True:
    numero = int(input("Ingrese un numero (0 para terminar): "))
    numeros_ingresados.append(numero)
    if numero == 0:
        break

print(f"Lista final de numeros: {numeros_ingresados}")

suma = 0
for num in numeros_ingresados:
    suma += num

print(f"Suma de todos los numeros ingresados: {suma}")