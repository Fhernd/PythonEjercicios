# Ejercicio 35: Crear una función únicamente para sumar números enteros.


def sumar(x, y):
    """
    Suma dos números. Valida que estos números sean enteros.
    """
    if isinstance(x, int) and isinstance(y, int):
        return x + y
    else:
        raise TypeError('Los valores deben ser enteros.')


try:
    print(sumar(2, 3))
    print(sumar(2, '3'))
except TypeError as e:
    print(e)