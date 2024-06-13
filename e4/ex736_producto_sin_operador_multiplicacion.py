# Ejercicio 736: Multiplicar dos números sin usar el operador de multiplicación (*).

# Recursividad.

# a*b = a_1 + a_2 + a_3 + ... + a_b

def multiplicar(a, b):
    if b < 0:
        return -multiplicar(a, -b)
    elif b == 0:
        return 0
    elif b == 1:
        return a
    else:
        return a + multiplicar(a, b - 1)


if __name__ == "__main__":
    resultado = multiplicar(3, -2)
    print(resultado)
    resultado = multiplicar(3, 2)
    print(resultado)
