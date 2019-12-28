# Ejercicio 144: Comprobar si una variable es entero o cadena de caracteres.

a = 13

print(isinstance(a, int) or isinstance(a, str))

a = '13'

print(isinstance(a, int) or isinstance(a, str))

a = [13]

print(isinstance(a, int) or isinstance(a, str))
