# Ejercicio 350: Concatenar los elementos de una lista por un carácter específico.

def concatenar_lista(lista, caracter):
    if isinstance(lista, list):
        if isinstance(caracter, str):
            return caracter.join(map(str, lista))

        raise TypeError('El parámetro caracter debe ser una cadena de caracteres (str).')

    raise TypeError('El parámetro lista debe ser una lista.')


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

resultado = concatenar_lista(numeros, '/')
print(resultado)
