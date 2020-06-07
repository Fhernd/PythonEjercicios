# Ejercicio 793: Usar accesores de una lista en una cadena de formato.

# numeros = [2, 3, 5, 7]
# numeros[0]
# numeros[1]
# numeros[-1]

numeros = [2, 3, 5, 7, 11, 13]

print(numeros)

print()

print(numeros[-1])
print('{l[1]}, {l[3]}, {l[5]}'.format(l=numeros))
