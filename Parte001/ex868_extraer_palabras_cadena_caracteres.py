# Ejercicio 868: Extraer las palabras que inician con mayúscula desde un texto.

import re

texto = 'PythonEsUnLenguajeDeProgramación'

patron = '[A-Z][^A-Z]*'

resultado = re.findall(patron, texto)

print(resultado)
