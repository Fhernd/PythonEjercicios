# Ejercicio 808: Leer el contenido completo de un archivo de texto plano.

ruta = 'Parte001/palabras_ingles.txt'

with open(ruta, 'r') as f:
    for l in f.readlines():
        print('Palabra: %s' % l)
