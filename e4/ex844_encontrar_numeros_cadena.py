# Ejercicio 844: Encontrar números enteros de hasta 3 cifras en una cadena de caracteres.

import re

frase = 'Algunos ejemplos de números primos: 1429, 11, 991, 67, 1033, 2, 3, y 5'

patron = r'\b\d{1,3}\b'

resultado = re.finditer(patron, frase)

for n in resultado:
    print(n.group(0))
