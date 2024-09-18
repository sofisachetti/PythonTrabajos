# Crear un diccionario con informacion de una persona
persona = {
    'nombre' : 'Catalina',
    'edad' : 33,
    'ciudad' : 'Bogota'
}

# Acceder a los elementos usando corchetes
nombre = persona['nombre']
edad = persona['edad']
ciudad = persona['ciudad']

# Imprimir os valores de cada uno
print("Nombre:", nombre)
print("Edad:", edad)
print("Ciudad:", ciudad)

# Intentar acceder a una clave que no existe
print(persona['pais']) # En consola sale: KeyError: 'pais'