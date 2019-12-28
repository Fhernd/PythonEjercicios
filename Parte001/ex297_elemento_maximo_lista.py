# Ejercicio 297: Crear función para encontrar el valor máximo en una lista de valores.

def maximo(valores):
    mayor = valores[0]

    for i in range(1, len(valores)):
        if valores[i] > mayor:
            mayor = valores[i]
    
    return mayor


numeros = [7, 11, 2, 0, 13, 5, -1, -8]

print(maximo(numeros))
