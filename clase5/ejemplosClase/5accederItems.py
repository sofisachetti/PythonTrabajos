# Crear diccionario
persona = {
    'nombre' : 'Alejandra',
    'edad' : 30,
    'ciudad' : 'Merida'
}

# usamos el metodo
pares_clave_valor = persona.items()

print("Pares clave-valor: ", pares_clave_valor)

lista = list(pares_clave_valor)
print("Valores como lista: ", lista)