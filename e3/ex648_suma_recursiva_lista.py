# Ejercicio 648: Crear función recursiva para sumar los elementos de una lista.

def sumar_lista(lista):
    if len(lista) == 0:
        return 0
    if len(lista) == 1:
        return lista[0]
    else:
        return lista[0] + sumar_lista(lista[1:])

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado = sumar_lista(numeros)
print('La suma de los valores de 1 a 5 es igual a %i' % resultado)

print()

primos = []
resultado = sumar_lista(primos)
print(resultado)
