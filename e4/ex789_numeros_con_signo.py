# Ejercicio 789: Agregar con una cadena de formato el signo de un número.

entero = 1000
real = 13.19

print(entero)
print(real)

# Mecanismo tradicional:
print('%+d' % (entero,))
print('%+f' % (real,))

# Mecanismo nuevo:
print('{:+d}'.format(entero))
print('{:+f}'.format(real))

print()

entero = -1000
real = -13.19

# Mecanismo tradicional:
print('%+d' % (entero,))
print('%+f' % (real,))

# Mecanismo nuevo:
print('{:+d}'.format(entero))
print('{:+f}'.format(real))

print()

print(entero)
print(real)
