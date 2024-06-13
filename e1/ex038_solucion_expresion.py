# Ejercicio 38: Resolver la expresión algebraica (x + y) * (x + y).

# (x + y) * (x + y) = x^2 + 2xy + y^2
# (2 + 3) * (2 + 3) = 5 * 5 = 25


def evaluar_expresion(x, y):
    """
    Resuelve la expresión algebraica (x + y) * (x + y).
    """
    return x**2 + 2 * x * y + y**2


x = float(input('Escriba el valor de x: '))
y = float(input('Escriba el valor de y: '))

print(evaluar_expresion(x, y))
