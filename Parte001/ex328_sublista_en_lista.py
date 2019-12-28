# Ejercicio 328: Comprobar si una lista contiene o no una sublista.

def es_sublista(lista, sublista):
    if len(sublista) == 0:
        return True
    if lista == sublista:
        return True
    if len(sublista) > len(lista):
        return False
    
    for v in sublista:
        if v not in lista:
            return False
    
    return True


lista_1 = [1, 2, 3, 4]
lista_2 = [3, 4]
print(es_sublista(lista_1, lista_2))

lista_3 = [3, 4, 5]
print(es_sublista(lista_1, lista_3))

lista_4 = [1, 2, 3, 4, 5]
print(es_sublista(lista_1, lista_4))

print(es_sublista(lista_1, []))
