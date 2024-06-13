# Ejercicio 902: Leer un archivo de texto en formato CSV (Valores Separados por Comas).

import csv

nombre_archivo = 'Parte001/Casos_positivos_de_COVID-19_en_Colombia.csv'

with open(nombre_archivo, newline='', encoding='utf-8') as f:
    datos = csv.reader(f, delimiter=',', quotechar=';')

    for r in datos:
        print(r)
