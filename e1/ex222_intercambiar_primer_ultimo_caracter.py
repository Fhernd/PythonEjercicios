# Ejercicio 222: Intercambiar el primer y último carácter de una cadena de caracteres.

# Solución:

# Python => nythoP


def intercambiar_caracteres(cadena):
    return cadena[-1] + cadena[1:-1] + cadena[0]


texto = 'Python'

print(intercambiar_caracteres(texto))
