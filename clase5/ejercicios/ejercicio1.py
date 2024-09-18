libro = {
    'titulo' : 'Orgullo y Prejuicio',
    'autor' : 'Jane Austen',
    'anio' : 1813,
    'genero' : 'Romance'
}

titulo = libro['titulo']
autor = libro.get('autor')
anio = libro['anio']
genero = libro.get('genero')

print("Titulo del libro: ", titulo)
print("Autor: ", autor)
print("Año de publicacion: ", anio)
print("Genero: ", genero)