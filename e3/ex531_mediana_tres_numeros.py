# Ejercicio 531: Crear una función personalizada para calcular la mediana de tres números.

def calcular_mediana(a, b, c):
    if a > b:
        if a < c:
            return a
        elif b > c:
            return b
        else:
            return c
    else:
        if a > c:
            return a
        elif b < c:
            return b
        else:
            return c


print(calcular_mediana(3, 7, 5))
print(calcular_mediana(3, 7, 9))
print(calcular_mediana(-3, -7, -5))
