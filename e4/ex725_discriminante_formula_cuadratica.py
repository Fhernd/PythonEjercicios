# Ejercicio 725: Crear función para calcular el número de soluciones de una fórmula cuadrática.

# a*x^2 + b*x + c => a, b, c

def discriminante(a, b, c):
    resultado = b**2 - 4 * a * c

    return resultado

def numero_soluciones(a, b, c):
    det = discriminante(a, b, c)

    if det > 0:
        return 2
    elif det == 0:
        return 1
    else:
        return 0

print(numero_soluciones(1, 0, 1))
print(numero_soluciones(1, 0, 0))
print(numero_soluciones(1, 0, -1))
