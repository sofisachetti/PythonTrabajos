# Ejercicio 8: Usar raise
# Crea un programa que solicite el ingreso de un número entre 1 y 10. Si el
# número no está en ese rango, genera una excepción con raise.

numero = int(input("Ingrese un numero: "))

if numero < 1 or numero > 10:
    raise ValueError("Debe ingresar un numero entre el 1 y el 10.")
print(f"Su numero es: {numero}")