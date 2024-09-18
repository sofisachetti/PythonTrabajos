persona = {
    'nombre' : 'Alejandra',
    'edad' : 30,
    'ciudad' : 'Merida',
    'profesion' : 'Ingeniera'
}

print("Diccionario original:", persona)

#Usamos popitem()
ultimo_elemento = persona.popitem()

print("Ultimo par clave-valor eliminado: ", ultimo_elemento)

# Imprimir diccionario despues de popitem
print("Diccionario despues de usar popItem:", persona)