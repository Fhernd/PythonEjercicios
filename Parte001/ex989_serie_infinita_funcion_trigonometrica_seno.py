# Ejercicio 989: Definir una función para calcular el seno de un ángulo dado usando una serie infinita.

import math

x = math.pi / 2

seno = 0

for n in range(0, 50):
    seno += math.pow(-1, n) / math.factorial(2 * n + 1) * math.pow(x, 2*n + 1)

print('El seno de pi/2 es igual a:', seno)
print('El seno de pi/2 es igual a:', math.sin(x))
