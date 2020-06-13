# Ejercicio 820: Comprobar si un archivo está abierto con la propiedad closed.

nombre_archivo = 'Parte001/ciudades.txt'

archivo = open(nombre_archivo, 'r', encoding='utf-8')

print(archivo.closed)

archivo.close()

print(archivo.closed)
