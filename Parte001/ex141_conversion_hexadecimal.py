# Ejercicio 141: Convertir un número entero a un número hexadecimal.

entero = 255

# Conversión numérica con la función hex:

hexadecimal = hex(entero)

print(type(hexadecimal))
print(hexadecimal)

print()

# Conversión a través de la función format:

hexadecimal = format(entero, '0x')

print(type(hexadecimal))
print(hexadecimal)
