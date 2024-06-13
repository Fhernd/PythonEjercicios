# Ejercicio 262: Generar todas las permutaciones con repetición posibles de una cadena.

from itertools import product

def permutaciones_repeticion(cadena, tamagnio):
    caracteres = list(cadena)
    permutaciones = []

    for c in product(caracteres, repeat=tamagnio):
        permutaciones.append(c)
    
    return permutaciones


texto = 'abc'
tamagnio = 3

print(permutaciones_repeticion(texto, tamagnio))

print()

print(permutaciones_repeticion(texto, 2))
