# Ejercicio 264: Encontrar el primer carácter repetido más cercano de una cadena.

# Solución:

# Python es tremendo

def caracter_repitido_cercano(cadena):
    auxiliar = []

    for c in cadena:
        if c in auxiliar:
            return c
        else:
            auxiliar.append(c)
    
    return None


texto = 'Python es tremendo'

print(caracter_repitido_cercano(texto))
print(caracter_repitido_cercano(texto) == ' ')
