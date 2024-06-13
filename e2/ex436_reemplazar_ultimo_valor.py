# Ejercicio 436: Reemplazar el último valor de cada tupla de una lista.

tuplas = [(10, 20, 30), (40, 50, 60), (70, 80, 90)]

print(tuplas)

tuplas = [t[0:-1] + (1000,) for t in tuplas]

print(tuplas)
