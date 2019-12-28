# Ejercicio 39: Calcular el valor futuro para una cantidad, interés, y número de años específicos.

def valor_futuro(vp, i, n):
    """
    Calcula el valor futuro.
    """
    return vp * (1 + i) ** n


valor_presente = 10000
interes = 3.5
periodos = 7

print(valor_futuro(valor_presente,  interes/100, periodos))
