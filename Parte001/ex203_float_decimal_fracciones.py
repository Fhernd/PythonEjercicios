# Ejercicio 203: Crear una fracción a partir de un número decimal o punto flotante.

# Solución:

# 0.5 => 1/2
# 0.3333333... => 1/3

from fractions import Fraction

decimal = 0.5

un_medio = Fraction(decimal)

print(decimal)
print(un_medio)

numero = '7e-5'

fraccion = Fraction(numero)

print(numero)
print(fraccion)
