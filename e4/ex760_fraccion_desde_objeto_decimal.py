# Ejercicio 760: Convertir un objeto Decimal en un objeto Fraction (fracción).

from decimal import Decimal
from fractions import Fraction

decimales = [Decimal(0.5), Decimal(0.25), Decimal(1/7), Decimal('5.0')]

for d in decimales:
    print('{} = {}'.format(d, Fraction(d)))
