# Ejercicio 60: Calcular la longitud de la hipotenusa de un triángulo rectángulo.

from math import sqrt

ab = float(input('Escriba el valor de la longitud del vértice AB: '))
bc = float(input('Escriba el valor de la longitud del vértice BC: '))

hipotenusa = sqrt(ab**2 + bc**2)

print('La longitud de la hipotenusa es: {}'.format(hipotenusa))
