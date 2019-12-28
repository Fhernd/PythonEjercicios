# Ejercicio 181: Calcular la suma de los dígitos de dos números.


def suma_digitos(numero):
    return sum([int(c) for c in str(numero)])


def suma_digitos_numeros(numero_1, numero_2):
    if isinstance(numero_1, int) and isinstance(numero_2, int):
        suma_1 = suma_digitos(numero_1)
        suma_2 = suma_digitos(numero_2)

        return suma_1 + suma_2
    else:
        raise TypeError('Los números deben ser enteros.')


x = 13
y = 29

print(suma_digitos_numeros(x, y))

x = 13.5

print(suma_digitos_numeros(x, y))
