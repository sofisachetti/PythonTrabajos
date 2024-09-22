# Ejercicio 5: Manejo de Matrículas en una Tupla
# • Crea una tupla llamada matriculas con los siguientes números de matrícula: (101, 102, 103, 104, 105).
# • Usa el método count para contar cuántas veces aparece el número de matrícula 102 en la tupla.
# • Usa el método index para encontrar la posición del número de matrícula 104 en la tupla.

matriculas = (101, 102, 103, 104, 105)

matricula_102 = matriculas.count(102)
print(f"Cantidad de veces que la matrícula 102 aparece en la tupla: {matricula_102}")

posicion_104 = matriculas.index(104)
print(f"La matrícula 104 está en la posición {posicion_104} dentro de la tupla.")