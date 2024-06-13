# Ejercicio 151: Comprobar si todos los elementos de una lista son distintos.

# [2, 3, 2, 5, 1] => {2, 3, 5, 1}


def elementos_distintos(datos):
    return len(datos) == len(set(datos))


lista = [2, 3, 2, 5, 1]
print(elementos_distintos(lista))

lista = [2, 3, 5, 7]
print(elementos_distintos(lista))
