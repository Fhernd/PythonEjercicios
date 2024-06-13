# Ejercicio 618: Seleccionar de forma aleatoria una palabra desde un archivo de texto plano.

import random

def seleccionar_palabra_aleatoria(nombre_archivo):
    palabras = []

    with open(nombre_archivo, 'r') as f:
        palabra = f.readline().strip()
        palabras.append(palabra)

        while palabra:
            palabra = f.readline().strip()
            palabras.append(palabra)
    
    return random.choice(palabras)

for _ in range(10):
    print(seleccionar_palabra_aleatoria('Parte001/palabras_ingles.txt'))
