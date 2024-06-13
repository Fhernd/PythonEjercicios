# Ejercicio 237: Comprobar con str.endswith si una cadena termina con texto específico.

texto = 'Python versión 3.8.0'

print(texto.endswith('3.8.0'))
print(texto.endswith(' 3.8.0'))
print(texto.endswith('  3.8.0'))
print(texto.endswith('n 3.8.0'))
print(texto.endswith('N 3.8.0'))
