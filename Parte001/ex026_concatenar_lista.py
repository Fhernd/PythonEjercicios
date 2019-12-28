# Ejercicio 26: Emular el funcionamiento de join para concatenar una lista.

# numeros = [2, 3, 5, 7, 11]

# 235711

# print(''.join([str(n) for n in numeros]))


def concatenar_lista(lista):
    resultado = ''

    for n in lista:
        resultado += str(n)
    
    return resultado


numeros = [2, 3, 5, 7, 11]

print(concatenar_lista(numeros))
