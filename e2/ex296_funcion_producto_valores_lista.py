# Ejercicio 296: Crear una función para multiplicar todos los elementos de una lista.

def multiplicar_lista(numeros):
    """
    Multiplica un conjunto de valores numéricos.
    """
    producto = 1

    for numero in numeros:
        producto *= numero
    
    return producto


numeros = [1, 2, 3, 4, 5]
print(multiplicar_lista(numeros))

numeros = [1.1, 2.2, 3.3, 4.4, 5.5]
print(multiplicar_lista(numeros))
