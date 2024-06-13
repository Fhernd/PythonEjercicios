# Ejercicio 131: Crear variables a partir de los valores de una lista.

numeros = [2, 3, 5, 7]

dos, tres = numeros[0:2]

print(dos, tres)

print()

tres, siete = numeros[1], numeros[-1]

print(tres, siete)

print()

tres, _, siete = numeros[1:]

print(tres, siete)
