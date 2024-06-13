# Ejercicio 269: Obtener el carácter más recurrente de una cadena de caracteres.

def caracter_mas_recurrente(frase):
    contador = [0] * 256

    for c in frase:
        contador[ord(c)] += 1
    
    maximo = -1
    caracter = ''

    for c in frase:
        if maximo < contador[ord(c)]:
            maximo = contador[ord(c)]
            caracter = c

    return caracter


cadena = 'aabbxxxxyy'
print(caracter_mas_recurrente(cadena))
