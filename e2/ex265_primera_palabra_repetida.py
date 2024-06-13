# Ejercicio 265: Encontrar la primera palabra repetida en una frase.

def primera_palabra_repetida(frase):
    auxiliar = set()

    for p in frase.split():
        if p in auxiliar:
            return p
        else:
            auxiliar.add(p)
    
    return None


cadena = 'Python es un lenguaje de programación. Python v. 3.8.0'
print(primera_palabra_repetida(cadena))

print()

cadena = 'Python es tremendo'
print(primera_palabra_repetida(cadena))

print()

cadena = 'Python es tremendo. Visual Studio Code es un editor liviano. Python es interpretado'
print(primera_palabra_repetida(cadena))
