# Ejercicio 154: Obtener las tripletas de números diferentes cuya suma es cero.

from itertools import permutations


def obtener_tripletas(numeros):
    if len(numeros) == 3:
        if len(set(numeros)) == 3:
            if sum(numeros) == 0:
                return [tuple(numeros)]
            else:
                return []
        else:
            return []
    else:
        perms = permutations(numeros, 3)
        tripletas = []
        for perm in list(perms):
            if len(set(perm)) == 3 and sum(perm) == 0:
                tripletas.append(perm)
        
        return tripletas


lista = [0, -2, 0, -1, 2, 4, -6, 1]
print(obtener_tripletas(lista))
