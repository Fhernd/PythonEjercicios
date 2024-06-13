# Ejercicio 876: Agregar espacio en blanco entre palabras de una cadena de caracteres.

import re

def separar_palabras(frase):
    patron = r'(\w)([A-Z])'

    return re.sub(patron, r'\1 \2', frase)


cadena = 'PythonEsUnLenguajeDeProgramación'
print(cadena)

print()

resultado = separar_palabras(cadena)

print(resultado)
