# Ejercicio 527: Determinar si un triángulo es equilátero, isósceles o escaleno.

def tipo_triangulo(a, b, c):
    if a == b and a == c:
        return 'Equilátero'
    elif a != b and a != c:
        return 'Escaleno'
    else:
        return 'Isósceles'


lado_1 = 5
lado_2 = 5
lado_3 = 5
print(tipo_triangulo(lado_1, lado_2, lado_3))

lado_1 = 5
lado_2 = 3
lado_3 = 5
print(tipo_triangulo(lado_1, lado_2, lado_3))

lado_1 = 5
lado_2 = 15
lado_3 = 10
print(tipo_triangulo(lado_1, lado_2, lado_3))
