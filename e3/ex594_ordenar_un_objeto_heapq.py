# Ejercicio 594: Crear una función para ordenar una estructura de datos heapq.

import heapq

def ordenar(lista):
    cola = []

    for e in lista:
        heapq.heappush(cola, e)
    
    return [heapq.heappop(cola) for i in range(len(cola))]


numeros = [1, 2, 5, 7, 9, 2, 5, 4, 6, 8, 10]
print(numeros)

resultado = ordenar(numeros)
print(resultado)
