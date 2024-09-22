#  verificar si un numero es par o impar usando operador ternario

numero = int(input("Ingrese un número: "))

mensaje = "Par" if numero % 2 == 0 else "Impar"
print(mensaje)