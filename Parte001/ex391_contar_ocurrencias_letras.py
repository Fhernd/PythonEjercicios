# Ejercicio 391: Contar las ocurrencias de las letras de una frase sobre un diccionario.

frase = 'python es tremendo'

resultado = {}

for c in frase:
    resultado[c] = resultado.get(c, 0) + 1

print(resultado)
