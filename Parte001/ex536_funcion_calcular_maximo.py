# Ejercicio 536: Crear una función personalizada para calcular el máximo de tres números.

def maximo_dos_numeros(a, b):
    if a > b:
        return a
    return b

def maximo_tres_numeros(a, b, c):
    return maximo_dos_numeros(a, maximo_dos_numeros(b, c))


print(maximo_tres_numeros(7, 5, 3))
print(maximo_tres_numeros(-7, -5, -3))
print(maximo_tres_numeros(11, 3, 19))
