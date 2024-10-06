# 6. Metodos de clase

# Definimos una clase
class Conejo:
    cantidad_de_conejos = 0 # Atributo de clase
    
    def __init__(self, color, nombre):
        self.color = color
        self.nombre = nombre
        Conejo.cantidad_de_conejos += 1 # Aumenta la cantidad total de conejos

    # Metodo de clase para obtener el total de conejos
    @classmethod
    def tota_conejos(cls):
        return f"Total de conejos: {cls.cantidad_de_conejos}"

# Crear instancias de la clase conejo
conejo1 = Conejo("blanco", "Tambor")
conejo2 = Conejo("gris", "Pochoclo")

# Llamar al metodo de clase
print(Conejo.tota_conejos())

# La clase conejo incluye un metodo de clase total_conejos, que se utiliza para acceder a una atributo de clase (cantidad_de_conejos).
# Este metodo permite realizar operaciones que afectan a la clase en su totalidad, en lugar de a instancias individuales.
# Lo que facilita el seguimiento de cuantos objetos de esa clase han sido creados.
