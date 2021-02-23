# Ejercicio 967: Generar una lista con los valores intercalados procedentes de diferentes listas.

from itertools import chain

def elementos_intercalados(*datos):
    resultado = list(chain(*zip(*datos)))

    return resultado

numeros_1 = [1000, 2000, 3000, 4000, 5000, 6000, 7000]
numeros_2 = [100, 200, 300, 400, 500]
numeros_3 = [10, 20, 30]

# [1000, 100, 10, 2000, 200, 20, 3000, 300, 30]

resultado = elementos_intercalados(numeros_1, numeros_2, numeros_3)
print(resultado)
