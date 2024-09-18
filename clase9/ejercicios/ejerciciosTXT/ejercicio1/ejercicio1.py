#definir el nombre del archivo
mi_archivo = 'mi_archivo.txt'

with open(mi_archivo, 'r') as file:
    print('Leyendo todas las lineas de una vez con readlines(): ')
    lineas = file.readlines()
    for linea in lineas:
        print(linea.strip())