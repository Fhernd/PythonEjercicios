# Ejercicio 253: Mostrar la posición de cada carácter en una cadena con enumerate.

cadena = 'Python 3.8.0'

for i, c in enumerate(cadena):
    print('Carácter: %s - Índice: %i' % (c, i))
