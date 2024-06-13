# Ejercicio 555: Contar la cantidad de variables locales declaradas en una función.

def funcion(a, b):
    x = 1
    y = 2
    lenguaje = 'Python'
    print(x, y, lenguaje)


print(funcion.__code__.co_nlocals)
