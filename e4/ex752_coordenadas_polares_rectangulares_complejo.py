# Ejercicio 752: Calcular las coordenadas polares y rectangulares de un número complejo.

import cmath

complejo = complex(2, 3) # 2+3j

coordenadas_polares = cmath.polar(complejo)
print(coordenadas_polares)

print()

coordenadas_rectangulares = cmath.rect(coordenadas_polares[0], coordenadas_polares[1])
print(coordenadas_rectangulares)
