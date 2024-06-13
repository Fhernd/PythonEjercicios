# Ejercicio 57: Medir el tiempo de ejecución de un método.

import time


def sumar_rango(n):
    t_0 = time.time()
    
    suma = 0

    for i in range(1, n + 1):
        suma += i
    
    t_1 = time.time()

    return suma, t_1 - t_0


n = 100000

print(sumar_rango(n))

n = 1000000

print(sumar_rango(n))
