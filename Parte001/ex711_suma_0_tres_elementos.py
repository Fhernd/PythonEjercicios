# Ejercicio 711: Encontrar los 3 elementos que suman cero (0) desde una lista de números.

from itertools import combinations

def elementos_suma_cero(numeros):
    sublistas_tres = list(combinations(numeros, 3))
    sublistas = []

    for s in sublistas_tres:
        if sum(s) == 0:
            sublistas.append(s)
    
    return sublistas

numeros = [-3, 2, 1, 7, -4, -1, -2, 7, 5, -3, 0, 11, -11]
resultado = elementos_suma_cero(numeros)

print(resultado)
