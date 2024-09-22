# Ejercicio 4: Clasificación de Alumnos
# Escribe un programa que clasifique a los alumnos en dos listas: aprobados
# y desaprobados, según sus calificaciones.
# Instrucciones:
# • Define una lista con las calificaciones de los alumnos.
# • Define dos listas vacías: aprobados y desaprobados.
# • Usa un bucle para recorrer la lista de calificaciones.
# • Si la calificación es 60 o más, añade el nombre del alumno a la lista
# de aprobados, si no, añádelo a desaprobados.
# • Muestra las listas de aprobados y desaprobados.

#Lista de alumnos
lista_alumnos = ['Ana', 'Juan', 'Maria', 'Luis', 'Carmen']
lista_calificaciones = [85, 55, 90, 40, 70]

aprobado = []
desaprobado = []

for i in range(len(lista_alumnos)):
    if lista_calificaciones[i] > 60:
        aprobado.append(lista_alumnos[i])
    else:
        desaprobado.append(lista_alumnos[i])

print(f"Alumnos aprobados: {aprobado}")
print(f"Alumnos desaprobados: {desaprobado}")