# Ejercicio 1: Calificación con Operador Ternario
# Escribe un programa que asigna un mensaje a una variable resultado
# basado en una calificación (entre 0 y 100). Usa el operador ternario
# para asignar "Aprobado" si la calificación es mayor o igual a 60 y
# "Reprobado" en caso contrario.


resultado = int(input('Ingrese la calificación: '))

if (resultado > 100) or (resultado < 0):
    print('El valor ingresado no es correcto. Debe ingresar una nota entre 0 y 100.')
elif resultado >= 60:
    print('Está aprobado')
else:
    print('Reprobado')