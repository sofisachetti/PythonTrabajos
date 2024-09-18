# Creamos diccionario
estudiante = {
    'nombre' : 'Laura',
    'edad' : 22,
    'curso' : 'Ingenieria',
    'ciudad' : 'Barcelona'
}

# Imprimimos el diccionario
print("Diccionario original:", estudiante)

# Eliminar elemento con la clave 'curso' usando del
del estudiante['curso']
print("Diccionario modificado: ", estudiante)