# Ejercicio 2: Escribir en un archivo TXT
# Crea un programa que escriba un texto en un archivo nuevo_archivo.txt. Si
# el archivo ya existe, debe sobrescribir su contenido.

with open('nuevo_archivo.txt', 'w') as file:
    file.write("Las chicas de Python escribieron en este archivo.")
print('Archivo escrito con exito. ')