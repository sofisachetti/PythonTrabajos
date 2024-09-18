# Ejemplo de diccionario
diccionario_vacio = {}
print('Ejemplo de un diccionario vacio: ', diccionario_vacio)

# Ejemplo básico de un diccionario
persona = {
    'nombre' : 'Maria',
    'edad' : 30,
    'casada' : False,
    'hijos' : ['Ana', 'Luis'], # Esto de acá es una lista
    'direccion' : { #Acá puedo poner un diccionario dentro de otro
        'calle' : 'La Gran Via',
        'cuidad' : 'Madrid'
    }
}
print("Ejemplo de diccionario basico: ", persona)

# Ejemplo de diccionario con valores de distintos tipos
diccionario_mixto = {
    'nombre' : 'Alejandra',
    1 : [2, 3 , 4], #Clave es un entero, valor es un string
    (2, 3) : 'tupla como clave' # Clave es una tupla y valor un string
}
print('Ejemplo de diccionario mixto: ', diccionario_mixto)