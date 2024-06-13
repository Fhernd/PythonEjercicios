# Ejercicio 182: Determinar el tipo de triángulo (isósceles, escaleno, equilatero) dados tres lados.

# Solución:


def tipo_triangulo(a, b, c):
    if a == b and a == c:
        return 'Equilatero'
    elif a != b and a != c:
        return 'Escaleno'
    else:
        return 'Isósceles'


print(tipo_triangulo(7, 7, 7))
print(tipo_triangulo(7, 7, 9))
print(tipo_triangulo(7, 8, 9))
