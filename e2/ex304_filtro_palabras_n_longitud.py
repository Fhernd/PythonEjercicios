# Ejercicio 304: Crear función para obtener las palabras de n longitud.

def palabras_n_longitud(palabras, n):
    resultado = []

    for p in palabras:
        if len(p) == n:
            resultado.append(p)
    
    return resultado


lenguajes = ['Python', 'Java', 'C++', 'C', 'JavaScript', 'PHP']
longitud = 3

print(palabras_n_longitud(lenguajes, longitud))
