# Ejercicio 815: Encontrar el tamaño en bytes de un archivo de texto plano.

from os import stat

def calcular_tamagnio(archivo):
    try:
        informacion_archivo = stat(archivo)

        return informacion_archivo.st_size
    except FileNotFoundError:
        return None


nombre_archivo = 'Parte001/lorem.txt'
resultado = calcular_tamagnio(nombre_archivo)

print(resultado)
