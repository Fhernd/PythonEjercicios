# Ejercicio 392: Imprimir el contenido de un diccionario en una tabla.

valores = {'C1': [1, 2, 3], 'C2': [5, 6, 7], 'C3': [9, 10, 11]}

for fila in zip(*([k] + (v) for k, v in sorted(valores.items()))):
    print(*fila)
