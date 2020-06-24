# Ejercicio 865: Remover todo el espacio en blanco en una cadena de caracteres.

import re

texto = '       Python es un                lenguaje           de    programación           '

print(texto)

print()

patron = r'\s+'

resultado = re.sub(patron, '', texto)

print(resultado)
