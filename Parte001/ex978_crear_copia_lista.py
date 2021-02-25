# Ejercicio 978: Crear una copia completa de una lista con notación de slicing y la función copy().

letras = list('PYTHON')
print(letras) # ['P', 'Y', 'T', 'H', 'O', 'N']

print()

print('ID de la lista letras:', id(letras))

print()

letras_2 = letras[:]
print(letras_2)
print(id(letras_2))

print()

letras_3 = letras.copy()
print(letras_3)
print(id(letras_3))
