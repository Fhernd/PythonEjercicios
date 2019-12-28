# Ejercicio 305: Crear función básica para comprobar si 2 listas tienen un valor en común.

def listas_elemento_comun(lista_1, lista_2):
    for v1 in lista_1:
        for v2 in lista_2:
            if v1 == v2:
                return True

    return False

numeros_1 = [2, 3, 5, 7, 11]
numeros_2 = [3, 9, 12, 6, 18]
print(listas_elemento_comun(numeros_1, numeros_2))

numeros_3 = [-5, -4, -3]
print(listas_elemento_comun(numeros_1, numeros_3))
