# Ejercicio 9: Buscar y Imprimir la Edad de un Estudiante en un Diccionario Anidado
# 1. Crea un diccionario que represente una clase con los siguientes datos:
# o nombre_clase
# o estudiantes, que es una lista de diccionarios con información de cada estudiante (nombre y edad).
# 2. Escribe una función que busque la edad de un estudiante dado su
# nombre usando el índice de la lista en lugar de bucles (suponiendo que conoces el índice).
# 3. Imprime la edad del estudiante buscado.

clase = {
    'materia': 'Literatura',
    'alumnos': [
        {'nombre': 'Ana', 'edad': 17},
        {'nombre': 'Pedro', 'edad': 16},
        {'nombre': 'Juan', 'edad': 17},
        {'nombre': 'Maria', 'edad': 15},
        {'nombre': 'Soledad', 'edad': 16},
        {'nombre': 'Belen', 'edad': 17}
    ]
}

indice = int(input('Ingrese el indice del alumno: '))
nombre = input('Ingrese el nombre del alumno: ')

def buscarAlumno(indice, nombre):
    alumno = clase['alumnos'][indice]
    if alumno['nombre'] == nombre:
        print(f"La edad de {nombre} es {clase['alumnos'][indice]['edad']}")
    else: 
        print('Alumno no encontrado.')

print(buscarAlumno(indice, nombre))