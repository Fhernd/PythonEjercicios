# Ejercicio 460: Ingresar n palabras y contar las ocurrencias de cada palabra.

from collections import Counter, OrderedDict

class ContadorOrdenado(Counter, OrderedDict):
    pass


n = int(input('Cantidad de palabras: '))
palabras = []

for _ in range(n):
    palabras.append(input().strip())

contador = ContadorOrdenado(palabras)

print(contador)
print(len(contador))

print()

for c in contador:
    print(contador[c], end=' ')
