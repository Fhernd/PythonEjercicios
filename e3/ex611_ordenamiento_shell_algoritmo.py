# Ejercicio 611: Crear una función para el algoritmo de ordenamiento shell.

def shell(lista):
    mitad = len(lista) // 2

    while mitad > 0:
        for p in range(mitad):
            reducir_busqueda(lista, p, mitad)

        mitad = mitad // 2


def reducir_busqueda(lista, inicio, salto):
    for i in range(inicio + salto, len(lista), salto):
        valor = lista[i]
        posicion = i

        while posicion >= salto and lista[posicion - salto] > valor:
            lista[posicion] = lista[posicion - salto]
            posicion = posicion - salto
        
        lista[posicion] = valor


numeros = [7, 2, 11, 3, 1, 13, 5]
print(numeros)

shell(numeros)
print(numeros)
