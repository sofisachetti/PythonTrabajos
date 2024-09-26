# Ejercicio 7: Contar Ocurrencias de Elementos en un Diccionario Anidado
# 1. Crea un diccionario que contenga información sobre tres clubes
# deportivos, cada uno con una lista de jugadores.
# o Cada jugador es un diccionario con las claves: nombre y edad.
# 2. Cuenta cuántos jugadores en total tienen cada uno de los clubes

clubes = {
    'Amistad y Union' : [
        {'nombre': 'Pedro', 'edad': 20},
        {'nombre': 'Ana', 'edad': 18},
        {'nombre': 'Luis', 'edad': 18},
        {'nombre': 'Florencia', 'edad': 16}
    ],
    'Nautico' : [
        {'nombre': 'Maria', 'edad': 16},
        {'nombre': 'Jose', 'edad': 17}
    ],
    'Bancario' : [
        {'nombre': 'Juan', 'edad': 19},
        {'nombre': 'Liusina', 'edad': 20},
        {'nombre': 'Felipe', 'edad': 20}
    ]
}

print(f"Cantidad de jugadores en el Club Amistad y Union: {len(clubes['Amistad y Union'])}")
print(f"Cantidad de jugadores en el Nautico: {len(clubes['Nautico'])}")
print(f"Cantidad de jugadores en el Club Bancario: {len(clubes['Bancario'])}")