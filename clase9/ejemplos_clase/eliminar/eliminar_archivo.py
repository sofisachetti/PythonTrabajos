import os  # Lo primero que se hace, es modulo nativo

# Definimos el nombre del archivo
nombre_archivo = 'archivo.txt'

# Comprobar si el archivo existe en la ruta especificada+
# La funcion os.path.exist() devuelve true si el archivo existe y false en caso contrario
if os.path.exists(nombre_archivo):
    #si el archivo existe procedera a eliminarlo y a funcion os.remove() elimina el archivo en la ruta especificada
    os.remove(nombre_archivo)
    print(f"Archivo '{nombre_archivo}' elimanado.")
else:
    #si el archivo no existe informar al usuario que no se encontro nada
    print(f"El archivo '{nombre_archivo}' no existe.")