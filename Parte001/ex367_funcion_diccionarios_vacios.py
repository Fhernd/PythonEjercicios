# Ejercicio 367: Crear función para comprobar si los diccionarios de una lista están vacíos.

def diccionarios_vacios(lista):
    """
    Comprueba si una lista de diccionarios se halla vacía.
    """
    return all(not d for d in lista)


lista = [{}, {}, {}, {}]
resultado = diccionarios_vacios(lista)
print(resultado)

lista = [{}, {}, {}, {1: 'Python'}]
resultado = diccionarios_vacios(lista)
print(resultado)
