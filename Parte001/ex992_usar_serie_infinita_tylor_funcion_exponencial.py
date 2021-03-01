# Ejercicio 992: Definir la función exponencial a partir de una serie infinita de Taylor.

import math

def funcion_exponencial(x):
    suma = 0

    for n in range(0, 50):
        suma += math.pow(x, n) / math.factorial(n)

    return suma

print('Resultado con la función funcion_exponencial:', funcion_exponencial(2))
print('Resultado con la función math.exp:', math.exp(2))
