# Ejercicio 69: Ordenar tres números de menor a mayor sin usar condicionales ni ciclos.

x = int(input('Escriba el primer número: '))
y = int(input('Escriba el segundo número: '))
z = int(input('Escriba el tercer número: '))

a = min(x, y, z)
c = max(x, y, z)
b = (x + y + z) - a - c

# 1, 2, 3
# a = 1
# c = 3
# b = (1 + 2 + 3) - 1 - 3
# b = 6 - 1 - 3 = 2

print('Los números ordenados son: {}, {} y {}'.format(a, b, c))
