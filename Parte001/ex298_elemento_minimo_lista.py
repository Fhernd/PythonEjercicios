# Ejercicio 298: Crear función para encontrar el valor mínimo en una lista de valores.

def valor_minimo(valores):
    """
    Calcular el valor mínimo de una lista de valores numéricos.
    """
    minimo = valores[0]

    for i in range(1, len(valores)):
        if valores[i] < minimo:
            minimo = valores[i]

    return minimo


numeros = [13, 11, 23, 2, 5, 29, 7]
print(valor_minimo(numeros))

numeros = [5.5, 3.3, 9.7, 1.7, 9.3, 17.11]
print(valor_minimo(numeros))
