import os

nombre_archivo = 'archivo_para_eliminar.txt'

if os.path.exists(nombre_archivo):
    os.remove(nombre_archivo)
    print(f'El archivo "{nombre_archivo}" fue eliminado con exito.')
else:
    print(f'El archivo "{nombre_archivo}" no existe.')