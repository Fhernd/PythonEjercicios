# Ejercicio 5: Obtener la representación inversa de una cadena de caracteres.

# Python => nohtyP

cadena = 'Python'

for i in range(len(cadena) - 1, -1, -1):
    print(cadena[i], end='')

print()

print(cadena[::-1])
