# Paso 1: definimos nombre archivo
nombre_archivo = 'archivo.txt'

# Paso 2: leemos todo el contenido de una sola vez
with open(nombre_archivo, 'r') as archivo:
    print("Leyendo el archivo de una vez con read():")
    contenido_completo = archivo.read()
    print(contenido_completo)
    print("-" * 40)

# Paso 3: leer el archivo linea por linea
with open(nombre_archivo, 'r') as archivo:
    print("Leyendo el archivo de linea por linea con readline():")
    linea = archivo.readline()
    while linea:
        print(linea.strip())
        linea = archivo.readline()
    print("-" * 40)

# Paso 4: leer todas las lineas a la vez con readlines():
with open(nombre_archivo, 'r') as archivo:
    print("Leer todas las lineas a la vez con readlines():")
    lineas = archivo.readlines()
    for linea in lineas:
        print(linea.strip())
    print("-" * 40)