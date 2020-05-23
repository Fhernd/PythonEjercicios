# Ejercicio 778: Uso de la función join() para concatenar un conjunto de valores tipo string.

# Conjunto -> Lista, tupla

nombres = ['Juan', 'Oliva', 'Daniela', 'Edward', 'Germán']

print('Contenido de la variable `nombres`:', nombres)

print()

formato = ', '.join(nombres)

print('Contenido de la variable `formato`:', formato)

print()

numeros = [2, 3, 5, 7, 11, 13, 17, 19]

print('Contenido de la variable `numeros`:', numeros)

print()

# formato = ', '.join(numeros) # TypeError

formato = ', '.join([str(n) for n in numeros])

print('Contenido de la variable `formato`:', formato)
