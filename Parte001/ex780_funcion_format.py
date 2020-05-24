# Ejercicio 780: Uso de la función format() para formatear una cadena de caracteres.

uno = 1
dos = 2

print('{}, {}'.format(uno, dos)) # 1, 2

print('{1}, {0}'.format(uno, dos)) # 2, 1

print('{1}, {0}'.format(dos, uno)) # 1, 2

print('{1}, {0}, {2}'.format(dos, uno, dos)) # 1, 2, 2

print('{1}, {0}, {0}'.format(dos, uno)) # 1, 2, 2
