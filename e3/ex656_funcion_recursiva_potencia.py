# Ejercicio 656: Crear una función recursiva para calcular la potencia de un número.

# a^b = a_1 * a_2 * a_3 * ... * a_b

def potencia(a, b):
    if b == 0:
        return 1
    elif a == 0:
        return 0
    elif b == 1:
        return a
    else:
        return a * potencia(a, b - 1)

# 2 ^ 4 = 16
print(potencia(2, 4))
# 4 ^ 3 = 4 * 4 * 4 = 64
print(potencia(4, 3))
# 3 ^ 4 = 3 * 3 * 3 * 3 = 81
print(potencia(3, 4))
