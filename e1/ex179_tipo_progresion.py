# Ejercicio 179: Identificar el tipo de progresión (aritmética o geométrica) a partir de una lista.

# Solución:

# Progresión aritmética: [1, 2, 3, 4] => incremento unitario, [2, 4, 6, 8, 10]

# Progresión geométrica: [2, 6, 18, 54]


def identificar_progresion(numeros):
    if sum(numeros) == 0:
        return None
    else:
        if numeros[1] - numeros[0] == numeros[2] - numeros[1]:
            return 'Aritmética'
        else:
            return 'Geométrica'


print(identificar_progresion([1, 2, 3, 4]))
print(identificar_progresion([0, 0, 0]))
print(identificar_progresion([2, 6, 18, 54]))
