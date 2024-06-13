# Ejercicio 909: Omitir el encabezado de un archivo CSV con la función next().

import csv

ruta_archivo = 'Parte001/paises.csv'

with open(ruta_archivo, newline='', encoding='utf-8') as f:
    paises = csv.reader(f, delimiter='\t', skipinitialspace=True)

    next(paises)

    for p in paises:
        print(p)
