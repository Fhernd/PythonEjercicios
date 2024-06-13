# Ejercicio 607: Crear una función para el algoritmo de búsqueda secuencial sobre una lista.

def busqueda_secuencial(lista, valor):

    posicion = 0
    encontrado = False

    while posicion < len(lista) and not encontrado:
        if lista[posicion] == valor:
            encontrado = True
        else:
            posicion += 1
    
    return encontrado, posicion


numeros = [2, 7, 3, 5, 13, 31, 29, 17, 19]
llave = 37
print(busqueda_secuencial(numeros, llave))

llave = 5
print(busqueda_secuencial(numeros, llave))

llave = 19
print(busqueda_secuencial(numeros, llave))
