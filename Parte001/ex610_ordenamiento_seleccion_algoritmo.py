# Ejercicio 610: Crear una función para el algoritmo de ordenamiento por selección.

def ordenamiento_seleccion(lista):
    for n in range(len(lista) - 1, 0, -1):
        posicion_maxima = 0

        for l in range(1, n + 1):
            if lista[l] > lista[posicion_maxima]:
                posicion_maxima = l
        
        temp = lista[n]
        lista[n] = lista[posicion_maxima]
        lista[posicion_maxima] = temp


numeros = [19, 17, 2, 29, 3, 5, 11, 7, 13]
print(numeros)

ordenamiento_seleccion(numeros)
print(numeros)
