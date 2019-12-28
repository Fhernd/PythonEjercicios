# Ejercicio 91: Alternar el contenido de dos variables.

a = 2
b = 3

# a = 3, b = 2

print(a, b)

temp = a
a = b
b = temp

print(a, b)

print()

a = 2
b = 3

print(a, b)

a, b = b, a
# a, b = (b, a)

print(a, b)
