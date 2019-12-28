# Ejercicio 157: Contar las ocurrencias de las letras en un archivo de texto plano.

import collections
import pprint

nombre_archivo = 'crimen_castigo.txt'


with open(nombre_archivo, 'r') as f:
    conteo_caracteres = collections.Counter(f.read().upper())
    salida = pprint.pformat(conteo_caracteres)

# print(conteo_caracteres)
print(salida)
