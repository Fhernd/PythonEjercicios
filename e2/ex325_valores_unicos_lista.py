# Ejercicio 325: Crear función para obtener los elementos únicos de una lista.

def valores_unicos(lista):
    return list(set(lista))


numeros = [2, 3, 3, 5, 7, 0, 0, 1, 11, 13, 13, 13]

resultado = valores_unicos(numeros)

print(numeros)
print(resultado)
