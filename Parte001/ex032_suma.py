# Ejercicio 32: Calcular la suma de tres números si todos son diferentes, en caso contrario la suma será 0.


def sumar(x, y, z):
    """
    Suma tres números. Si al menos dos números son iguales, la suma será 0.
    """
    if x == y or x == z or y == z:
        return 0
    else:
        return x + y + z


print(sumar(2, 5, 3))
print(sumar(2, 5, 2))
print(sumar(5, 5, 2))
print(sumar(11, 7, 5))
