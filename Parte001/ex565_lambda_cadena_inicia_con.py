# Ejercicio 565: Crear una función lambda para validar si una cadena inicia con un carácter.

inicia_con = lambda c: True if c.startswith('P') else False

cadena = 'Python'
print(inicia_con(cadena))

print()

print(inicia_con('python'))
