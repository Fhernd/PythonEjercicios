# Ejercicio 277: Encontrar la subcadena mínima que contenga otra cadena de caracteres.

import collections

def subcadena_minima(frase, cadena):
    contador = collections.Counter(frase)
    longitud = len(cadena)
    i = 0
    p = 0
    q = 0

    for j, c in enumerate(frase, 1):
        longitud -= contador[c] > 0
        contador[c] -= 1

        if not longitud:
            while i < q and contador[frase[i]] < 0:
                contador[frase[i]] += 1
                i += 1
            
            if not q or j - i <= q - p:
                p, q = i, j
    
    return frase[p+1:q+1]

print(subcadena_minima('caballo', 'aba'))
