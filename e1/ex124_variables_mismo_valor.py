# Ejercicio 124: Comprobar si múltiples variables contienen el mismo valor.

a, b, c = 50, 50, 50

print(a, b, c)

if a == b and a == c:
    print('Sí, son iguales')

if a == b == c:
    print('Sí, son iguales')
