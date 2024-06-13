# Ejercicio 614: Crear una función para el algoritmo de ordenamiento por cuentas.

def ordenamiento_cuentas(lista):
    maximo = max(lista) + 1
    conteo = [0] * maximo

    for n in lista:
        conteo[n] += 1
    
    i = 0

    for j in range(maximo):
        for k in range(conteo[j]):
            lista[i] = j
            i += 1
    
    return lista

numeros = [2, 3, 8, 4, 3, 2, 5, 3, 4, 3, 2]
print(numeros)

numeros = ordenamiento_cuentas(numeros)
print(numeros)
