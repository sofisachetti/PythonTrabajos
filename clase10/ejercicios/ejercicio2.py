# 2. Clases de Formas Geométricas
#  Define una clase base Forma con un método area(). Luego, crea subclases Rectangulo, Circulo, y Triangulo que implementen el método area() de manera específica. 
# Usa polimorfismo para crear una lista de formas y calcular el área de cada una.

class Forma:
    def area(self):
        print("El area de la forma elegida es:")

class Rectangulo(Forma):
    def __init__(self, alto, ancho):
        self.alto = alto,
        self.ancho = ancho
    
    def area(self):
        return self.alto * self.ancho

class Circulo(Forma):
    def __init__(self, radio):
        self.radio = radio
    
    def area(self):
        return 3.14 * self.radio ** 2

class Triangulo(Forma):
    def __init__(self, base, alto):
        self.base = base,
        self.alto = alto
    
    def area(self):
        return (self.alto * self.base) / 2

