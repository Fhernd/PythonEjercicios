# Ejercicio 170: Encontrar el valor medio entre tres números.

# 3, 9, 7 => 3, 7, 9

x = int(input('Digite el primer número: '))
y = int(input('Digite el segundo número: '))
z = int(input('Digite el tercer número: '))

# Solución no. 1:
menor = min(x, y, z)
mayor = max(x, y, z)
valor_medio = (x + y + z) - menor - mayor

print(menor, valor_medio, mayor)

print()

# Solución no. 2:
numeros = [x, y, z]
print(numeros)
numeros = sorted(numeros)
print(numeros)
