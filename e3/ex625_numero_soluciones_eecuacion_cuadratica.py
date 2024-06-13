# Ejercicio 625: Crear una función para contar cuántas soluciones tiene una ecuación cuadrática.

# a*x^2 + b*x + c = 0

def soluciones_ecuacion_cuadratica(coeficientes):
    a = coeficientes[0]
    b = coeficientes[1]
    c = coeficientes[2]
    determinante = b**2 - 4 * a * c
    if determinante >= 0:
        if a != 0:
            if determinante == 0:
                return 1
            else:
                return 2
        else:
            return 0
    else:
        return 0

print(soluciones_ecuacion_cuadratica((1, 0, 1)))
print(soluciones_ecuacion_cuadratica((1, 0, 0)))
print(soluciones_ecuacion_cuadratica((1, 0, -1)))
