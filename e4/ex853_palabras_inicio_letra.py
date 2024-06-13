# Ejercicio 853: Encontrar dos palabras que empiecen con la misma letra en un listado.

import re

lenguajes = ['C C++', 'Java JavaScript', 'Ruby R', 'Python PHP']

for l in lenguajes:
    resultado = re.match('(P\w+)\W(P\w+)', l)

    if resultado:
        print(resultado.groups())
