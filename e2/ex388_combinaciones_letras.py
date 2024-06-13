# Ejercicio 388: Crear todas las combinaciones de letras de los elementos de diccionarios.

from itertools import product

dict_letras = {'1': ['w', 'x'], '2': ['y', 'z']}

for c in product(*[dict_letras[k] for k in sorted(dict_letras.keys())]):
    print(''.join(c))
