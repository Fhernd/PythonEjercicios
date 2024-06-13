# Ejercicio 877: Remover los caracteres en minúscula desde una cadena usando una expresión regular.

import re

texto = 'AbCdefGHiJklmnOPQrstuvWXYz'

print(texto)

print()

patron = '[a-z]'

resultado = re.sub(patron, '', texto)

print(resultado)
