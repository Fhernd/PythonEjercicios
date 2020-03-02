# Ejercicio 720: Crear una función para calcular el área de un paralelogramo.

def area_paralelogramo(b, h):
    """
    Calcula el área de un paralelogramo.
    """
    area = b * h

    return area

base = float(input('Digite la base del paralelogramo: '))
altura = float(input('Digite la altura del paralelogramo: '))

resultado = area_paralelogramo(base, altura)

print(f'El área del paralelogramo es igual a {resultado}.')
