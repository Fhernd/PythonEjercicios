# Ejercicio 774: Usar el operador del para borrar una variable declarada.

print('x' in dir())

print()

x = 100

print('x' in dir())

print()

del x

print('x' in dir())

try:
    del x
except NameError as e:
    print(e)
