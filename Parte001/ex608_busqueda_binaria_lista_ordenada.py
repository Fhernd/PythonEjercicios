# Ejercicio 608: Crear función para el algoritmo para búsqueda binaria en una lista ordenada.

def busqueda_binaria_lista_ordenada(lista, valor):
    if len(lista) == 0:
        return False
    else:
        mitad = len(lista) // 2

        if lista[mitad] == valor:
            return True
        else:
            if valor < lista[mitad]:
                return busqueda_binaria(lista[:mitad], valor)
            else:
                return busqueda_binaria(lista[mitad + 1:], valor)


def busqueda_binaria(lista, valor):
    primero = 0
    ultimo = len(lista) - 1
    encontrado = False

    while primero <= ultimo and not encontrado:
        mitad = (primero + ultimo) // 2

        if lista[mitad] == valor:
            encontrado = True
        else:
            if valor < lista[mitad]:
                ultimo = mitad - 1
            else:
                primero = mitad + 1
    
    return encontrado


numeros = [2, 3, 5, 7, 11, 13, 17, 19, 23, 27, 29, 31]
llave = 37
print(busqueda_binaria_lista_ordenada(numeros, llave))

llave = 11
print(busqueda_binaria_lista_ordenada(numeros, llave))

print(busqueda_binaria_lista_ordenada([], llave))
