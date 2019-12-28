# Ejercicio 121: Determinar si una variable está definida o no.

try:
    division = 5 / x

    print(division)
except NameError as e:
    print('No se pudo realizar la división. Una variable no existe: %s' % e)
else:
    print('La operación se realizó de forma satisfactoria.')

print('...')

x = 3

try:
    division = 5 / x

    print(division)
except NameError as e:
    print('No se pudo realizar la división. Una variable no existe: %s' % e)
else:
    print('La operación se realizó de forma satisfactoria.')

print('---')
