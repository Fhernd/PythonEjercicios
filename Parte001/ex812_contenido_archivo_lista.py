# Ejercicio 812: Leer todo el contenido de un archivo con readlines() sobre una lista.

def leer_archivo(archivo):
    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            return f.readlines()
    except FileNotFoundError as e:
        print('El archivo no existe.')

nombre_archivo = 'Parte001/ciudades.txt'

resultado = leer_archivo(nombre_archivo)

print(resultado)

print()

resultado = [c.replace('\n', '') for c in resultado]

print(resultado)
