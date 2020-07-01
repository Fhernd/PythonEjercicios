# Ejercicio 905: Leer un archivo CSV sobre una estructura de datos tipo diccionario.

import csv

nombre_archivo = 'Parte001/Casos_positivos_de_COVID-19_en_Colombia_100.csv'

with open(nombre_archivo, newline='', encoding='utf-8') as f:
    covid_19_colombia = csv.DictReader(f)

    for r in covid_19_colombia:
        print(r)
