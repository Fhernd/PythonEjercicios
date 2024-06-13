# Ejercicio 759: Crear objetos Fraction para obtener la representación fraccionario de un decimal.

import fractions

decimales = [0.7, 2.5, 0.5, 9.32, 7e-1]

for d in decimales:
    fraccion = fractions.Fraction(d)
    print('{} = {}'.format(d, fraccion))
