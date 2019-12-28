# Ejercicio 120: Limitar la visualización del número de caracteres de una cadena.

lenguaje = '¡Python es tremendo!'

print(lenguaje)
print(lenguaje[0:7])
print(lenguaje[:7])

print('%.7s' % lenguaje)

print()

cadena = '123456789'

print(cadena[:6])
print('%.6s' % cadena)
