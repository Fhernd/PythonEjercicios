# Ejercicio 866: Remover todos los caracteres que representen símbolos en un texto.

import re

texto = 'Página oficial de Python (v. 3.8.0): https://www.python.org/.'

patron = '[\W]+'
regex = re.compile(patron)

resultado = regex.sub('', texto)

print(resultado)
