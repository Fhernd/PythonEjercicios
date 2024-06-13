# Ejercicio 347: Particionar una lista en sublistas cada n-ésimo elemento.

# Análisis:

# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# => [1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11]

from string import ascii_lowercase


def particionar_lista(lista, n):
    return [lista[i*n:i*n+n] for i in range(n)]

print(ascii_lowercase)

az = list(ascii_lowercase)

print(az)

print()

resultado = particionar_lista(az, 5)

print(resultado)
