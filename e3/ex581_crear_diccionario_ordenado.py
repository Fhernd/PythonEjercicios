# Ejercicio 581: Crear un diccionario ordenado con la clase OrderedDict.

from collections import OrderedDict

nombres = {'Daniela': 27, 'Edward': 29, 'Germán': 31, 'John': 35}

diccionario_ordenado = OrderedDict(nombres.items())

for k in diccionario_ordenado:
    print(k, diccionario_ordenado[k])

print()

for k in reversed(diccionario_ordenado):
    print(k, diccionario_ordenado[k])
