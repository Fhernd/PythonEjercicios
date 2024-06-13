# Ejercicio 1021: Contar la cantidad de ocurrencias de una letra por cada palabra en una lista de palabras.

nombres = ['Alexander', 'Deisy', 'Alexandra', 'Juan', 'Edgar', 'Oliva']

resultado = list(map(lambda n: n.count('a'), nombres))
print(resultado)    # [1, 0, 2, 1, 1, 1]
