# Ejercicio 189: Determinar si dos números (o su suma) superan los 80 dígitos.


def supera_limite(a, b):
    """
    Comprueba si uno o dos números superan un límite establecido.
    """
    return a >= 10**80 or b >= 10**80 or a + b >= 10**80


x = 10**81
y = 1

print(supera_limite(x, y))

x = 3

print(supera_limite(x, y))
