# Ejercicio 169: Uso de parámetros sólo posicionales en Python 3.8.0.

def funcion(a, b, /, c, d, *, e, f):
    return 0

funcion(1, 2, 3, d=4, e=5, f=6)

#funcion(1, b=2, 3, d=4, e=5, f=6)
#funcion(a=1, b=2, 3, d=4, e=5, f=6)
#funcion(1, 2, 3, d=4, 5, f=6)

def potencia(x, y, /):
    return x**y


potencia(2, 3)
