# Ejercicio 819: Leer una línea aleatoria desde un archivo de texto plano con choice().

from random import choice

def linea_aleatoria(archivo):
    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            lineas = f.read().splitlines()

            return choice(lineas)
    except FileNotFoundError:
        return None

nombre_archivo = 'Parte001/ciudades.txt'

resultado = linea_aleatoria(nombre_archivo)

print(resultado)
