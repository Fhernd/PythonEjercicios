# Ejercicio 153: Eliminar cada i-ésimo elemento de una lista.

# [1, 2, 3, 4, 5, 6, 7, 8] => [1, 3, 5, 7]
# [1, 3, 4, 5, 6, 7, 8]
# [1, 2, 3, 4, 5, 6, 7, 8] => [1, 2, 4, 5, 7, 8]
# [1, 2, 3, 4, 5, 6, 7, 8] => []


def eliminar_i_esimo_elemento(datos, iesimo=2):
    longitud = len(datos)
    if longitud > 0:
        cantidad_eliminar = longitud // iesimo
        iesimo -= 1
        indice = 0
        while cantidad_eliminar > 0:
            indice = (iesimo + indice) % longitud
            datos.pop(indice)
            longitud -= 1
            cantidad_eliminar -= 1


numeros = [1, 2, 3, 4, 5, 6, 7, 8]
print(numeros)
eliminar_i_esimo_elemento(numeros)
print(numeros)

print()

numeros = [1, 2, 3, 4, 5, 6, 7, 8]
print(numeros)
eliminar_i_esimo_elemento(numeros, 3)
print(numeros)

print()

numeros = [1, 2, 3, 4, 5, 6, 7, 8]
print(numeros)
eliminar_i_esimo_elemento(numeros, 10)
print(numeros)

print()

numeros = [1, 2, 3, 4, 5, 6, 7, 8]
print(numeros)
eliminar_i_esimo_elemento(numeros, 8)
print(numeros)

print()

numeros = [1, 2, 3, 4, 5, 6, 7, 8]
print(numeros)
eliminar_i_esimo_elemento(numeros, 1)
print(numeros)
