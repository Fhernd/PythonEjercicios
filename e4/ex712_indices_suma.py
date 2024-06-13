# Ejercicio 712: Encontrar dos índices de números que suman un valor particular.

# Análisis:
# [1, 2, 3, 4, 5], 6

def encontrar_indices_suma(numeros, suma):
    numeros_indices = {}

    for i, n in enumerate(numeros):
        if suma - n in numeros_indices:
            return numeros_indices[suma - n], i
        
        numeros_indices[n] = i


numeros = [1, 2, 3, 4, 5]
suma = 6
resultado = encontrar_indices_suma(numeros, suma)
print(resultado)

# Prueba de escritorio:
# numeros_indices = {1: 0, 2: 1, 3: 2, }
