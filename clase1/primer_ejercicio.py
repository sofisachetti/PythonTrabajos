# 1. Declaración de variables y constantes
edad = 25                   #Número
nombre = "Ana"              #Cadena de texto (String)
esta_estudiando = True      #Booleano

# Declaracion de constantes
PI = 3.14               #Numero
PAIS = "Argentina"      #Cadena de texto (String)

# 2. Leer valores por teclado
edad = int(input("introduce tu edad: "))                                    #Para leer numero entero
nombre = input("introduce tu nombre: ")                                     #Leer cadena de texto
esta_estudiando = input("¿Estás estudiando? (sí/no): ").lower() == "si"     #Leer y convertir a booleano

# 3. Tipos de datos
cantidad_de_libros = 10                              #Numero(int)
titulo_libro = "El Principito"                       #Cadena de texto (String)
es_interesante = True                                #Booleano(bool)
temas = ["Aventura", "Fantasia", "Filosofia"]        #Lista (array)
autor = {
    "nombre": "Antoine de Saint-Exupery",
    "nacionalidad" : "Francesa"
}

# Convertir tipos de datos
edad_str = str(edad)                                         #convertir numero a cadena de texto
cantidad_de_libros_float = float(cantidad_de_libros)         #convertir entero a numero de punto flotante

# 4. Imprimir resultados en la consola
print("Nombre", nombre)
print("Edad:", edad)
print("Está estudiando?", esta_estudiando)
print("Constante PI:", PI)
print("constante país:", PAIS)
print("Cantidad de libros", cantidad_de_libros)
print("Titulo del libro:", titulo_libro)
print("¿Es intersante?", es_interesante)
print("Temas del libro:",temas)
print("Autor del libro:", autor)
print("Edad (como cadena de texto):", edad_str)
print("Cantidad de libros (como float):", cantidad_de_libros_float)