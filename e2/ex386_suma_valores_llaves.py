# Ejercicio 386: Combinar dos diccionarios para sumar los valores de llaves comunes.

from collections import Counter

dict_1 = {'w': 100, 'x': 200, 'y': 300}
dict_2 = {'x': 200, 'y': 100, 'z': 100}

resultado = Counter(dict_1) + Counter(dict_2)

print(resultado)
