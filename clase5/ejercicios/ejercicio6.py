# Ejercicio 6: Anidación Compleja de Diccionarios y Listas
# 1. Crea un diccionario que contenga información sobre una escuela. La escuela tiene:
# o Nombre
# o Año de fundación
# o Lista de clases, donde cada clase es un diccionario con:
# ▪ Nombre de la clase
# ▪ Lista de estudiantes, donde cada estudiante es un diccionario con:
# ▪ Nombre
# ▪ Edad
# 2. Imprime el nombre del primer estudiante de la primera clase.

escuela = {
    'nombre' : 'Normal 1',
    'anio_fundacion' : 1874,
    'lista_clases' : {
        
        'clase1' : {
            'nombre_clase' : 'Matematica',
            'estudiantes' : {
                
                'estudiante1' : {
                    'nombre_est' : 'Clara',
                    'edad_est' : 15
                },
                
                'estudiante2' : {
                    'nombre_est' : 'Juan',
                    'edad_est' : 15,
                },
                
                'estudiante3' : {
                    'nombre_est' : 'Ana',
                    'edad:est' : 14
                },
                
                'estudiante4' : {
                    'nombre_est' : 'Federico',
                    'edad_est' : 15
                }
                
            }
        },
        
        'clase2' : {
            'nombre_clase' : 'Literatura',
            'estudiantes' : {
                
                'estudiante1' : {
                    'nombre_est' : 'Manuel',
                    'edad_est' : 14
                },
                
                'estudiante2' : {
                    'nombre_est' : 'Mara',
                    'edad_est': 15
                },
                
                'estudiante3' : {
                    'nombre_est' : 'Fernanda',
                    'edad_est' : 15
                }
            }
            
        }
        
    }
}

print(escuela['lista_clases']['clase1']['estudiantes']['estudiante1']['nombre_est'])