# 1. Definir una clase en python

# Definir una clase llamada coch
class Coche:
    # metodo __init__ es el constructor que se llama al crear un nuevo objeto
    def __init__(self, marca, modelo):
        # self es una referencia al objeto que estamos creando
        # Inicializamos los atributos de la instancia
        self.marca = marca # Atributo de instancia: guarda la marca del coche
        self.modelo = modelo # Atributo de instancia: guarda el modelo del coche

# La clase coche es una plantilla para crear objetos de tipo auto.
# Contiene un metodo constructor __init__ que inicializa os atributos especificos de cada coche
# Como por ejemplo: marca, modelo usando la referencia self para distinguir entre las propiedades del obejto y los parametros pasados al constructor
