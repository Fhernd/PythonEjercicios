# Ejercicio 908: Imprimir el valor asociado a determinadas columnas de un archivo CSV.

import csv

ruta_archivo = 'Parte001/Casos_positivos_de_COVID-19_en_Colombia_100.csv'

with open(ruta_archivo, newline='', encoding='utf-8') as f:
    covid_colombia = csv.DictReader(f)

    for r in covid_colombia:
        print(r['ID de caso'], r['Fecha de notificación'], r['Ciudad de ubicación'], r['atención'])
