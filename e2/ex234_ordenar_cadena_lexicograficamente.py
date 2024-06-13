# Ejercicio 234: Ordenar una cadena de caracteres de forma lexicográfica.

# Análisis:

# Python => hnoPty

def cadena_orden_lexicografico(cadena):
    return ''.join(sorted(cadena, key=str.upper))


texto = 'Python'
print(cadena_orden_lexicografico(texto))
