# Ejercicio 6: Manejo básico de errores con try/except
# Crea un programa que solicite al usuario que ingrese un número. Si el
# usuario ingresa algo que no es un número, muestra un mensaje de error
# usando try/except.

try:
    numero_usuario = int(input("Ingrese un numero: "))
    print(f"Su numero es {numero_usuario}")
except ValueError:
    print("Error: Entrada no valida. Debes introducir un numero entero.")