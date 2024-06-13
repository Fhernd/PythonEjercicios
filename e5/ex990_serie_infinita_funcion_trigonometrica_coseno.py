# Ejercicio 990: Definir una función para calcular el coseno de un ángulo usando una serie infinita.

from math import cos, factorial, pi, pow

x = pi / 2

coseno = 0

for k in range(0, 50):
    coseno += pow(-1, k)*pow(x, 2 * k) / factorial(2*k)

print('Coseno de pi/2 calculado con una serie infinita:', coseno)
print('Coseno de pi/2 calculado la función cos():', cos(x))
