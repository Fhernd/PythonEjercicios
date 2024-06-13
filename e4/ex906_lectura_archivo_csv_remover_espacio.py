# Ejercicio 906: Leer un archivo CSV y remover el espacio en blanco después del delimitador.

import csv

nombre_archivo = 'Parte001/paises.csv'

with open(nombre_archivo, newline='', encoding='utf-8') as f:
    paises = csv.reader(f, delimiter='\t', skipinitialspace=True)

    for p in paises:
        print(p)
