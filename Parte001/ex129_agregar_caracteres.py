# Ejercicio 129: Rellenar una cadena de caracteres con un carácter específico.

# Python => ***Python***

lenguaje = 'Python'

print(lenguaje)
print(lenguaje.rjust(6 + 3, '*'))
print(lenguaje.ljust(6 + 3, '*'))

print(lenguaje.rjust(6 + 3, '*').ljust(12, '*'))
