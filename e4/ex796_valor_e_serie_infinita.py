# Ejercicio 796: Calcular el valor de la constante e (Euler) con una serie infinita.

from math import e, fabs, factorial

def serie_infinita_e(epsilon):
    e = 0
    i = 3
    suma_1 = 2
    suma_2 = suma_1 + float(1/factorial(2))

    while fabs(suma_1 - suma_2) >= epsilon:
        suma_1 = suma_2
        suma_2 += float(1/factorial(i))
        i += 1

    return suma_2


print(serie_infinita_e(0.00000001))
print(e)
