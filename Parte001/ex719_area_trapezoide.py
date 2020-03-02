# Ejercicio 719: Crear una función personalizada para calcular el área de un trapezoide.

def area_trapezoide(B, b, h):
    """
    Calcula el área de un trapezoide.
    """
    area = (B + b) / 2 * h

    return area


print(area_trapezoide(5, 3, 7)) # 28.0
