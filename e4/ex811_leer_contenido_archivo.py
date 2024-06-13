# Ejercicio 811: Leer el contenido de un archivo por medio de la función readline().

nombre_archivo = 'Parte001/ciudades.txt'

with open(nombre_archivo, 'r', encoding='utf-8') as f:
    linea = f.readline()

    while linea:
        print(linea, end='')
        linea = f.readline()
