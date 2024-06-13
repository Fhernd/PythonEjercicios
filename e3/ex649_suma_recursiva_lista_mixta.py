# Ejercicio 649: Crear función recursiva para sumar los elementos de una lista mixta.

# [1, 2, [2, 3], [[4, 5]], [[[6]]]]

def sumar_lista_mixta(lista):
    total = 0
    for l in lista:
        if type(l) == type([]):
            total += sumar_lista_mixta(l)
        else:
            total += l
    
    return total


numeros = [1, 2, [2, 3], [[4, 5]], [[[6]]], [], []]
resultado = sumar_lista_mixta(numeros)
print(resultado)
