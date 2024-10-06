# 2. Propiedades de un objeto

# Definir clase persona:
class Persona:
    def __init__(self, nombre, edad):
        # inicializar las propiedades del objeto
        self.nombre = nombre
        self.edad = edad

# Crear un objeto de la clase Persona
persona1 = Persona("Ana", 30)
persona2 = Persona("Luis", 35)

# Acceder a las propidades del objeto
print(persona1.nombre)
print(persona1.edad)

print(persona2.nombre)
print(persona2.edad)

# La clase Persona define un objeto que tiene propiedades como nombre y edad
# Al instanciar persona1 con valores especificos, se crean atributos unicos que representan
# el estado de ese objeto
# Se puede acceder a estas propiedades utilizando la notacion de punto, lo que permite
# obtener informacion sobre la instancia creada.