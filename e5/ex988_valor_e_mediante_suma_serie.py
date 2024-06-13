# Ejercicio 988: Calcular el valor de la constante e (número de Euler) con la suma de serie infinita.

from math import factorial
import math

limite = 100

e = 0

for n in range(100):
    e += 1/factorial(n)

print('Constante de Euler (e):', e)
print('Constante de Euler (e):', math.e)
