# Ejercicio 166: Validar la prioridad de los operadores suma, resta, producto y división.

__prioridad__ = {
    '+': 0,
    '-': 0,
    '*': 1,
    '/': 1
}


def tiene_mayor_prioridad(operador_1, operador_2):
    return __prioridad__[operador_1] >= __prioridad__[operador_2]


# 3 + 7 - 3 = 7
print(tiene_mayor_prioridad('-', '+'))

# 3 * 7 - 3 = 18
print(tiene_mayor_prioridad('*', '+'))

print(tiene_mayor_prioridad('/', '*'))

print(tiene_mayor_prioridad('-', '/'))
