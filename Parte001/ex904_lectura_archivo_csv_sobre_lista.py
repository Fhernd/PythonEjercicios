# Ejercicio 904: Leer un archivo CSV sobre una estructura de datos lista.

import csv

nombre_archivo = 'Parte001/paises.csv'

with open(nombre_archivo, newline='') as f:
    datos = csv.reader(f, delimiter='\t')

    paises = list(datos)

print('El tipo de dato de la lista `paises` es:', type(paises))

print(paises)
