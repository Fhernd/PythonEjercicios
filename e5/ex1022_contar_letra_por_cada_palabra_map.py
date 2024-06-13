# Ejercicio 1022: Contar la cantidad de ocurrencias de una letra por cada palabra en una lista de palabras.

nombres = ['Alexander', 'Deisy', 'Alexandra', 'Juan', 'Edgar', 'Oliva']

# Alexander => a => 1
# Alexander => ALEXANDER => 2

resultado = list(map(lambda n: n.upper().count('A'), nombres))
print(resultado)    # [2, 0, 3, 1, 1, 1]
