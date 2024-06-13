# Ejercicio 229: Duplicar los n caracteres finales de una cadena de caracteres.

# Análisis:

# Python -> onon

def duplicar_ultimos_n_caracteres(cadena, n):
    if n <= len(cadena):
        return cadena[-n:] * 2
    else:
        raise ValueError('La cantidad de caracteres a duplicar sobrepasa la longitud de la cadena.')


cadena = 'Python'

print(duplicar_ultimos_n_caracteres(cadena, 2))
print(duplicar_ultimos_n_caracteres(cadena, 3)) # honhon
# print(duplicar_ultimos_n_caracteres(cadena, 20)) # Genera error
