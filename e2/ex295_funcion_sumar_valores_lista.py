# Ejercicio 295: Crear una función para sumar todos los elementos de una lista.

def sumar_lista(lista):
    """
    Suma un conjunto de valores en una lista.
    """
    suma = 0

    for numero in lista:
        suma += numero
    
    return suma


numeros = [1, 2, 3, 4, 5]

print(sumar_lista(numeros))

numeros = [1.1, 2.2, 3.3, 4.4, 5.5]

print(sumar_lista(numeros))
