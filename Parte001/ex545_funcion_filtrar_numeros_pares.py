# Ejercicio 545: Crear una función para filtrar los números pares de una lista o tupla.

def filtrar_pares(numeros):
    pares = []

    for n in numeros:
        if n % 2 == 0:
            pares.append(n)
    
    return pares


lista_numeros = list(range(1, 11))
print(type(lista_numeros))
resultado = filtrar_pares(lista_numeros)
print(resultado)

print()

tupla_numeros = tuple(range(1, 11))
print(type(tupla_numeros))
resultado = filtrar_pares(tupla_numeros)
print(resultado)
