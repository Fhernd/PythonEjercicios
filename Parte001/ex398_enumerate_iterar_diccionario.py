# Ejercicio 398: Usar la función enumerate() para iterar por los ítems de un diccionario.

diccionario = {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50}

for c, (k, v) in enumerate(diccionario.items(), 1):
    print(k, v, c)
