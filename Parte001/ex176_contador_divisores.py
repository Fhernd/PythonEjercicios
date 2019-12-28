# Ejercicio 176: Contar la cantidad de divisores de un número entero positivo.


# Solución #1:
def contar_divisores(n):
    contador_divisores = 0

    for i in range(1, n + 1):
        if n % i == 0:
            contador_divisores += 1
    
    return contador_divisores


# Solución #2:
def divisores(n):
    if isinstance(n, int):
        if n > 0:
            return len([i for i in range(1, n + 1) if n % i == 0])
        else:
            raise ValueError('El valor pasado no es un número positivo.')
    else:
        raise TypeError('El valor pasado como argumento no es un entero.')


print(contar_divisores(5))
print(contar_divisores(8))

print()

print(divisores(5))
print(divisores(8))

print()

try:
    print(divisores('5'))
except Exception as e:
    print(e)
