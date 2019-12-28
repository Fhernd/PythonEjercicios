# Ejercicio 202: Obtener el numerador y denominador de un objeto Fraction.

from fractions import Fraction

tres_medios = Fraction(2, 10)

print(tres_medios)

numerador = tres_medios.numerator

print('Numerador: %i' % numerador)

denominador = tres_medios.denominator

print('Denominador: %i' % denominador)
