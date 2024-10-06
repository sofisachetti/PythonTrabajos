# 1. Sistema de Gestión de Estudiantes
# o Crea una clase Estudiante con atributos como nombre, edad, y notas. Implementa métodos para calcular el promedio de notas
# y determinar si el estudiante ha aprobado o no. 
# Agrega una clase Curso que contenga una lista de estudiantes y un método para mostrar todos los estudiantes aprobados.

class Estudiante:
    def __init__(self, nombre, edad, notas):
        self.nombre = nombre
        self.edad = edad
        self.notas = notas

    def calcular_promedio(self):
        promedio = sum(self.notas) / len(self.notas)
        if promedio > 6:
            return "Aprobado"
        else:
            return "Desaprobado"

class Curso:
    estudiantes = [
        Estudiante("Luis", 13, [4, 5, 7]),
        Estudiante("Ana", 13, [5, 8, 3]),
        Estudiante("Jose", 13, [5, 8, 5]),
        Estudiante("Maria", 14, [6, 8, 10]),
        Estudiante("Florencia", 13, [7, 9, 7])
    ]

    @classmethod
    def mostrarAprobados(cls):
        aprobados = []
        for estudiante in cls.estudiantes:
            if Estudiante.calcular_promedio(estudiante) == "Aprobado":
                aprobados.append(estudiante)
        return aprobados

print(Curso.mostrarAprobados())