# Ejercicio 178: Computar la suma del valor absoluto de pares de elementos de una lista.

# Descripción: Computar la suma de la diferencia absoluta entre dos elementos de una lista. Los elementos deben estar ordenados de forma ascendente.

# Solución:

# [1, 2, 3]
# [1, 2], [1, 3], [2, 3]

from itertools import combinations


def suma_pares_diferentes(numeros):
    """
    Calcula la suma de pares diferente de una lista.
    """
    if isinstance(numeros, list):
        suma = 0

        for c in combinations(numeros, 2):
            suma += sum(c)

        return suma
    else:
        raise TypeError('El argumento pasado a la función no es una lista.')


lista = [1, 2, 3]

print(suma_pares_diferentes(lista))

#print(suma_pares_diferentes('1,2,3'))
