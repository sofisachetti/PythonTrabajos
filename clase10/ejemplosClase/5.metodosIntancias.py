# 5. Metodos instancias

# Definimos la clase
class Perro:
    def __init__(self, raza, nombre):
        self.raza = raza
        self.nombre = nombre
        
        # Metodo para mostrar info del perrito
    def mostrar_info(self):
        return f"Perro: {self.raza}, {self.nombre}"

# Crear un objeto de la clase Perro
mi_perro = Perro("mestizo", "Canela")

# Usar el metodo del objeto
print(mi_perro.mostrar_info())

# En la clase Perro el metodo mostrar_info() es un metodo de instancia que proporciona
# una representacion de la informacion del perro al acceder a sus atributos.
# Este metodo permite realizar acciones especificas sobre los datos del objeto como tal y se invoca
# atraves de la instancia de Perro para obtener detalles sobre ese obejto en particular.
