# Ejercicio 212: Sumar filas y columnas de una matriz y crear una nueva matriz.

def mostrar_matriz(matriz):
    for fila in matriz:
        print(fila)


matriz = [
    [25, 69, 51, 26],
    [68, 35, 29, 54],
    [54, 57, 45, 63],
    [61, 68, 47, 59]
]

mostrar_matriz(matriz)

filas = len(matriz)
columnas = len(matriz[0])

for i in range(filas):
    suma = sum(matriz[i])
    matriz[i].append(suma)

print()

mostrar_matriz(matriz)

print()

nueva_fila = []

for j in range(columnas):
    suma = sum([fila[j] for fila in matriz])
    nueva_fila.append(suma)

nueva_fila.append(sum(nueva_fila))

matriz.append(nueva_fila)

mostrar_matriz(matriz)
