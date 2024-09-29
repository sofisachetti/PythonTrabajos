# Ejercicio 7: Usar assert
# Crea un programa que pida al usuario ingresar su edad. Usa assert para
# verificar que la edad ingresada es mayor o igual a 18. Si no es así,
# muestra un mensaje de error.

edad = int(input("Ingrese su edad: "))
assert edad >= 18, "Error. Debe ser mayor de edad."
print(f"Su edad es: {edad}")
