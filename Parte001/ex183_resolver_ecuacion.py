# Ejercicio 183: Resolver un sistema de ecuaciones lineales.

# Solución:

# ax + by = c
# dx + ey = f


def solucion_sistema_ecuaciones(a, b, c, d, e, f):
    determinante = a*e - b*d

    if determinante != 0:
        x = (c*e - b*f) / determinante
        y = (a*f - c*d) / determinante

        return x, y
    else:
        return None, None


print('Digite los valores para a, b, c, d, e, y f: ')
a, b, c, d, e, f = map(float, input().split())

print(solucion_sistema_ecuaciones(a, b, c, d, e, f))
