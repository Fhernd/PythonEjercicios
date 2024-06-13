# Ejercicio 150: Comprobar si existe al menos un producto impar entre los elementos de una lista.


def es_producto_impar(numeros):
    for i in range(len(numeros)):
        for j in range(len(numeros)):
            if i != j:
                producto = numeros[i] * numeros[j]

                if producto & 1:
                    return True
    
    return False


datos = [2, 3, 7, 8, 1]
print(es_producto_impar(datos))

datos = [2, 4, 6]
print(es_producto_impar(datos))
