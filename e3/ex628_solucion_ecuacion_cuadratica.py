# Ejercicio 628: Crear una función para resolver una ecuación cuadrática.

# a*x^2 + b*x + c = 0
# a, b, c
from math import sqrt

def resolver_ecuacion(a, b, c):
    determinante = b**2 - 4*a*c

    if determinante > 0:
        x_1 = -b + sqrt(b**2 - 4*a*c) / (2*a)
        x_2 = -b - sqrt(b**2 - 4*a*c) / (2*a)
        return x_1, x_2
    elif determinante == 0:
        x_1 = -b / (2*a)
        return (x_1,)
    else:
        return tuple()


print(resolver_ecuacion(1, 0, 0))
print(resolver_ecuacion(1, 0, 1))
print(resolver_ecuacion(1, 0, -1))
