# Ejercicio 771: Obtener la parte entera y fraccionaria de un división de punto flotante.

# /: división de punto flotante
# //: división entera

from math import modf

print('{}(F)  (I)'.format(' ' * 10))

for i in range(6):
    print('{}/3 = {} {}'.format(i, i/3, modf(i/3.0)))
