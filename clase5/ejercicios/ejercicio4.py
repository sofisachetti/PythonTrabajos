lista_estudiantes = [
    {'nombre' : 'Sofia' , 'edad': 28, 'calificaciones': [6, 8 ,5, 9]},
    {'nombre' : 'Alejandra', 'edad' : 30, 'calificaciones' : [9, 6, 5, 7]},
    {'nombre' : 'Ana', 'edad' : 26, 'calificaciones' : [8, 2, 7, 7]},
    {'nombre' : 'Marcela', 'edad' : 27, 'calificaciones' : [5, 6, 6, 7]},
]

primer_estudiante = lista_estudiantes[0]
nombre_estudiante = primer_estudiante.get('nombre')
calificaciones_estudiante = primer_estudiante.get('calificaciones')
print(f"Nombre del estudiante: {nombre_estudiante}")
print(f"Calificaciones: {calificaciones_estudiante}")