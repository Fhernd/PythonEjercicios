# Ejercicio 18: Calcular la suma de tres números, e incluir una condición de igualdad.

def sumar_numeros(a, b, c):
    """
    Calcula la suma de tres números. Si los tres números son iguales, la suma 
    se multiplica por 3.
    """
    suma = a + b + c

    if a == b and a == c:
        suma *= 3
    
    return suma


print(sumar_numeros(2, 2, 7))
print(sumar_numeros(2, 2, 2))
