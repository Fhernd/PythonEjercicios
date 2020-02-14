# Ejercicio 624: Crear una función para validar si un número dado es Sastry.

# n = 183
# n + = 184
# 183184
# x ^ 2 = 183184
# 428

from math import isqrt, sqrt

def es_Sastry(numero):
    sucesor = numero + 1
    resultado = int('{}{}'.format(numero, sucesor))

    return isqrt(resultado) == sqrt(resultado)

print(es_Sastry(183))
print(es_Sastry(23))
