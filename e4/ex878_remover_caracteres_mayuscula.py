# Ejercicio 878: Remover los caracteres en mayúscula desde una cadena usando una expresión regular.

import re

texto = 'AbCdefGHiJklmnOPQrstuvWXYz'

print(texto)

print()

patron = '[A-Z]'

resultado = re.sub(patron, '', texto)

print(resultado)
