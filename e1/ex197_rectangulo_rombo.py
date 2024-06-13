# Ejercicio 197: Determinar si dos lados adyacentes y la diagonal corresponden a un rectángulo o rombo.

# Descripción: Determinar si dos lados adyacentes y la diagonal de un paralelogramo corresponden a un rectángulo o un rombo.

print('Escriba las longitudes de dos lados adyacentes y la diagonal: ', end='')
a, b, c = map(int, input().split(','))

if a**2 + b**2 == c**2:
    print('Los valores ingresados corresponden con un rectángulo.')
else:
    print('Los valores ingresados corresponden con un rombo.')
