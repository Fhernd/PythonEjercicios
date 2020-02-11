# Ejercicio 613: Crear una función para el algoritmo de ordenamiento quicksort.

def quick_sort(lista):
    quick_sort_auxiliar(lista, 0, len(lista) - 1)

def quick_sort_auxiliar(lista, inicio, fin):
    if inicio < fin:
        punto_particion = particionar(lista, inicio, fin)

        quick_sort_auxiliar(lista, inicio, punto_particion - 1)
        quick_sort_auxiliar(lista, punto_particion + 1, fin)

def particionar(lista, inicio, fin):
    pivote = lista[inicio]

    izquierda = inicio + 1
    derecha = fin
    terminado = False

    while not terminado:
        while izquierda <= derecha and lista[izquierda] <= pivote:
            izquierda += 1
        
        while lista[derecha] >= pivote and derecha >= izquierda:
            derecha -= 1
        
        if derecha < izquierda:
            terminado = True
        else:
            lista[izquierda], lista[derecha] = lista[derecha], lista[izquierda]
    
    lista[inicio], lista[derecha] = lista[derecha], lista[inicio]

    return derecha


numeros = [7, 3, 2, 13, 5, 7, 11, 1]
print(numeros)

quick_sort(numeros)
print(numeros)
