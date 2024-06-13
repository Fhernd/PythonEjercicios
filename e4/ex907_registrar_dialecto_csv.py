# Ejercicio 907: Registrar un dialecto (configuración) CSV con la función register_dialect().

import csv

csv.register_dialect('dialecto_basico', delimiter='\t', skipinitialspace=True)

ruta_archivo = 'Parte001/paises.csv'

with open(ruta_archivo, encoding='utf-8', newline='') as f:
    datos = csv.reader(f, dialect='dialecto_basico')

    for r in datos:
        print(r)
