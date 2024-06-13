# Ejercicio 260: Encontrar el primer carácter no repetido en una cadena de caracteres.

# Análisis:

# Python es tremendo. Python v. 3.8.0

def primer_caracter_no_repetido(cadena):
    conteo = {}

    for c in cadena:
        if c in conteo:
            conteo[c] += 1
        else:
            conteo[c] = 1
    
    for c in conteo.keys():
        if conteo[c] == 1:
            return c


texto = 'Python es tremendo'
print(primer_caracter_no_repetido(texto))

texto = 'Python es tremendo. Python v. 3.8.0'
print(primer_caracter_no_repetido(texto))
