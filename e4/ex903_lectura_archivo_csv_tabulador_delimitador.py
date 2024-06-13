# Ejercicio 903: Leer un archivo CSV donde el separador (delimitador) es el tabulador.

import csv

nombre_archivo = 'Parte001/paises.csv'

with open(nombre_archivo, newline='') as f:
    datos = csv.reader(f, delimiter='\t')

    for r in datos:
        print(', '.join(r))
