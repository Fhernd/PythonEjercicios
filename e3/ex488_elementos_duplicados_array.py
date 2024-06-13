# Ejercicio 488: Crear función para determinar si un objeto array contiene duplicados.

from array import array

def elementos_duplicados(arreglo):
    conjunto = set(arreglo.tolist())

    return len(conjunto) != len(arreglo)


numeros = array('i', [1, 2, 3, 4, 5])
print(elementos_duplicados(numeros))

numeros.append(1)
print(elementos_duplicados(numeros))
