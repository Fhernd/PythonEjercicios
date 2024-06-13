# Ejercicio 788: Agregar padding con especificadores de formato a valores numéricos.

entero = 1234
real = 3.141592653589793

print(entero)
print(real)

print()

# Mecanismo tradicional:
print('%d' % entero)
print('%f' % real)
print('%.10f' % real)

print()

# Mecanismo nuevo:

print('{:d}'.format(entero))
print('{:f}'.format(real))
print('{:.10f}'.format(real))

print()

# Padding a la izquierda:

print('{:<10d}entero'.format(entero))
print('{:<10f}real'.format(real))
print('{:<10.10f}real'.format(real))

# Padding a la derecha:
print()

print('{:>10d}entero'.format(entero))
print('{:>10f}real'.format(real))
print('{:>10.10f}real'.format(real))
