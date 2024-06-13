# Ejercicio 939: Usar la función truth() para validar si un conjunto de datos son equivalentes a True.

from operator import truth

datos = [True, False, 0, 'Cero', '', "", 1, None, """""", '        ']
print(datos)

print()

resultado = list(filter(truth, datos))
for r in resultado:
    print(r)

print()

resultado = list(filter(bool, datos))
for r in resultado:
    print(r)
