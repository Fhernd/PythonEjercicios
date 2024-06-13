# Ejercicio 329: Generar todas las sublistas posibles de una lista de valores con combinations.

from itertools import combinations

def generar_sublistas(lista):
    sublistas = []

    for i in range(0, len(lista) + 1):
        sublista = [list(c) for c in combinations(lista, i)]

        if len(sublista) > 0:
            sublistas.extend(sublista)
    
    return sublistas


numeros = [1, 2, 3, 4, 5]
resultado = generar_sublistas(numeros)
print(numeros)
print(resultado)

print()

lenguajes = ['Python', 'C++', 'PHP', 'C#', 'Java']
resultado = generar_sublistas(lenguajes)
print(lenguajes)
print(resultado)
