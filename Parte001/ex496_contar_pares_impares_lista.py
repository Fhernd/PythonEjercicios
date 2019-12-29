# Ejercicio 496: Crear función para contar la cantidad números pares e impares en una lista.

def contar_pares_impares(lista):
    pares, impares = 0, 0

    for n in lista:
        if n % 2 == 0:
            pares += 1
        else:
            impares += 1
    
    return pares, impares


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
resultado = contar_pares_impares(numeros)

print('La cantidad de pares es: %i' % resultado[0])
print('La cantidad de impares es: %i' % resultado[1])
