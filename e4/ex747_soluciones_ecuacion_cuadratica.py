# Ejercicio 747: Crear una función para encontrar las soluciones a una ecuación cuadrática.

from math import sqrt

# a*x**2 + b*x + c

def discriminante(a, b, c):
    return b**2 - 4 * a * c

def soluciones_ecuacion_cuadratica(a, b, c):
    d = discriminante(a, b, c)

    if d > 0:
        x_1 = (-b + sqrt(d)) / (2*a)
        x_2 = (-b - sqrt(d)) / (2*a)

        return x_1, x_2
    elif d == 0:
        x = -b / (2*a)

        return x,
    else:
        return tuple([])


if __name__ == "__main__":
    resultado = soluciones_ecuacion_cuadratica(1, 0, 1)
    print(resultado)
    resultado = soluciones_ecuacion_cuadratica(1, 0, 0)
    print(resultado)
    resultado = soluciones_ecuacion_cuadratica(1, 0, -1)
    print(resultado)
