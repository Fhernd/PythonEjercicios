# Ejercicio 359: Agregar contenido al principio de cada elemento de una lista.

def agregar_contenido(lista, contenido):
    """
    Agrega contenido al principio de cada elemento de una lista.
    """
    return ['{}{}'.format(contenido, e) for e in lista]


numeros = list(range(1, 11))
print(numeros)

resultado = agregar_contenido(numeros, 'id')
print(resultado)
