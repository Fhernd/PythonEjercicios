# Ejercicio 147: Comprobar si un número es múltiplo de otro.


def multiplo(a, b):
    """
    Comprueba si un número es múltiplo de otro.
    """
    return a % b == 0


print(multiplo(12, 6))
print(multiplo(13, 2))
