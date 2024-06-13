# Ejercicio 128: Comprobar si un carácter dado existe en una cadena de caracteres.

lenguaje = 'Python es tremendo!'

print(lenguaje.count('y') > 0)

print(any(c == 'y' for c in lenguaje))

print(any(c == 'x' for c in lenguaje))

print(lenguaje.count('x') > 0)

print()

print(lenguaje.count('p') > 0)
print(lenguaje.count('P') > 0)

print()

print(any(c.lower() == 'p' for c in lenguaje))
