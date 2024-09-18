persona = {
    'nombre' : 'Emilia',
    'edad' : 33,
    'ciudad' : 'CABA'
}

#Comprobar si una clave existe en el diccionario antes de acceder a su valor
clave = 'edad'

if clave in persona:
    valor = persona[clave]
    print(f"El valor de '{clave}' es: {valor}")
else:
    print(f"La clave '{clave}' no existe en el diccionario.")


#Intentar acceder a una clave que no existe
clave_inxistente = 'pais'

if clave_inxistente in persona:
    valor = persona[clave_inxistente]
    print(f"El valor de {clave_inxistente} es: {valor}")
else: 
    print(f"La clave '{clave_inxistente}' no existe en el diccionario.")


# Otra opcion de hacerlo. Muestra TRUE en la consola
print("nombre" in persona)