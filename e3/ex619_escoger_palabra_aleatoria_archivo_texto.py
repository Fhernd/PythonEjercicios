# Ejercicio 619: Seleccionar de forma aleatoria una palabra desde un archivo de texto plano.

import random

def seleccionar_palabra_aleatoria(nombre_archivo):

    with open(nombre_archivo, 'r') as f:
        palabras = list(f)
    
    return random.choice(palabras).strip()

for _ in range(10):
    print(seleccionar_palabra_aleatoria('Parte001/palabras_ingles.txt'))
