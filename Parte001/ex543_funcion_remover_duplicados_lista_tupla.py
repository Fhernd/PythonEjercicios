# Ejercicio 543: Crear una función para remover los duplicados de una lista o tupla.

def remover_duplicados(elementos):
    no_duplicados = []

    for e in elementos:
        if e not in no_duplicados:
            no_duplicados.append(e)
    
    return no_duplicados


lista_numeros = [2, 2, 3, 3, 3, 4, 5, 6, 7, 7, 7, 7, 7]
print(type(lista_numeros))
print(len(lista_numeros))
resultado = remover_duplicados(lista_numeros)
print(resultado)
print(len(resultado))

print()

tupla_numeros = (2, 2, 3, 3, 3, 4, 5, 6, 7, 7, 7, 7, 7)
print(type(tupla_numeros))
print(len(tupla_numeros))
resultado = remover_duplicados(tupla_numeros)
print(resultado)
print(len(resultado))
