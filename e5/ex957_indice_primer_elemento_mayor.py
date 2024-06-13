# Ejercicio 957: Obtener el índice del primer elemento que sea mayor a un elemento dado usando el módulo itertools.

from itertools import takewhile

def primer_elemento(numeros, numero):
    return len(list(takewhile(lambda c: c[1] <= numero, enumerate(numeros))))

primos = [19, 23, 2, 5, 89, 61, 59, 43, 7, 13]
n = 83

resultado = primer_elemento(primos, n)
print(resultado)    # 4

resultado = primer_elemento(primos, 3)
print(resultado)    # 0
