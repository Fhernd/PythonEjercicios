# Ejercicio 130: Determinar si una función dada es una función generadora.

from inspect import isgeneratorfunction

def funcion():
    return 'Python'


print(isgeneratorfunction(funcion))


def generar_pares():
    numero = 2
    yield numero

    while True:
        numero += 2
        yield numero


print(isgeneratorfunction(generar_pares))
