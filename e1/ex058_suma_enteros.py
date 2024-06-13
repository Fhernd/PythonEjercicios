# Ejercicio 58: Calcular la suma de los primeros n números enteros.

# Usando la fórmula de Gauss: n * (n + 1) / 2

n = 10

suma = n * (n + 1)/2

print(suma)

print()

# Usando un ciclo:
suma = 0

for i in range(1, n + 1):
    suma += i

print(suma)

print()

# Usar la función sum:

suma = sum(range(1, n + 1))

print(suma)
