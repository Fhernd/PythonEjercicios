# Ejercicio 537: Crear una función personalizada para sumar los números de una lista o tupla.

def sumar(numeros):
    suma = 0

    for n in numeros:
        suma += n
    
    return suma


lista_numeros = [1, 2, 3, 4, 5]
print(type(lista_numeros))
print(sumar(lista_numeros))

print()

tupla_numeros = (1, 2, 3, 4, 5)
print(type(tupla_numeros))
print(sumar(tupla_numeros))
