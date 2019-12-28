# Ejercicio 362: Encontrar la sublista con la mayor suma de sus elementos.

listas_numeros = [[8, 3, 1], [4, 8, 1], [8, 5, 2], [4, 11, 13], [-8, 14, 2]]

# 12, 13, 15, 28, 8

resultado = max(listas_numeros, key=sum)

print(resultado)
