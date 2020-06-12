# Ejercicio 814: Encontrar la frecuencia de palabras en una frase de un archivo de texto.

from collections import Counter

def encontrar_frecuencia(archivo):
    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            contenido = f.readline()
            palabras = contenido.split()

            return Counter(palabras)
    except FileNotFoundError:
        print('El archivo especificado no se ha encontrado.')


nombre_archivo = 'Parte001/lorem.txt'
conteo = encontrar_frecuencia(nombre_archivo)

print(conteo)
