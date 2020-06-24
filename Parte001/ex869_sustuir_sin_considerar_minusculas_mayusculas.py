# Ejercicio 869: Sustituir una cadena sin considerar mayúsculas ni minúsculas.

import re

texto = 'Python es un lenguaje de programación. Versión de PyThOn 3.8.0. ¡PYTHON es tremendo! python es multiparadigma.'

print(texto)

print()

regex = re.compile(re.escape('python'), re.IGNORECASE)

resultado = regex.sub('Python', texto)

print(resultado)
