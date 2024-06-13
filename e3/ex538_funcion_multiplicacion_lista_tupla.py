# Ejercicio 538: Crear una función para multiplicar los números de una lista o tupla.

def multiplicar(numeros):
    producto = 1

    for n in numeros:
        producto *= n
    
    return producto


lista_numeros = [2, 3, 5, 7, 11]
print(type(lista_numeros))
print(multiplicar(lista_numeros))

print()

tupla_numeros = (2, 3, 5, 7, 11)
print(type(tupla_numeros))
print(multiplicar(tupla_numeros))
