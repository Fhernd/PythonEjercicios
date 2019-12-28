# Ejercicio 149: Calcular la suma del cubo de cada número menor a un número n dado.

# n = 5, 1^3 + 2^2 + 3^3 + 4^3
# = 1 + 8 + 27 + 64 = 100


def suma_cubos(n):
    suma = 0
    n -= 1

    while n > 0:
        suma += n**3
        n -= 1
    
    return suma


n = 5

print(suma_cubos(n))

sumatoria_cubos = sum([i**3 for i in range(0, n)])

print(sumatoria_cubos)
