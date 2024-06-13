# Ejercicio 122: Gestión de una excepción tipo aritmética.

try:
    print(1/0)
except ZeroDivisionError as e:
    print(e)

print('...')
