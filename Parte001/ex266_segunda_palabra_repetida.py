# Ejercicio 266: Encontrar la segunda palabra más repetida en una frase.

def segunda_palabra_repetida(frase):
    contador = {}
    palabras = frase.split()

    for p in palabras:
        if p in contador:
            contador[p] += 1
        else:
            contador[p] = 1
    
    contador = sorted(contador.items(), key=lambda item: item[1])

    return contador[-2]


cadena = 'Python es un lenguaje de programación. Python es un lenguaje interpretado. Python v. 3.8.0. Lenguaje de programación... es un'

print(segunda_palabra_repetida(cadena))
