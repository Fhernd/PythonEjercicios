# Ejercicio 275: Obtener los caracteres comunes de dos cadenas de caracteres.

# Solución:

# Cadena 1: 'Python' - Cadena 2: PHP => P
# Cadena 1: 'JavaScript' - Cadena 2: Java => Java
# Cadena 1: 'Python' - Cadena 2: C++ => '' (None)

from collections import Counter

def caracteres_comunes(cadena_1, cadena_2):
    contador_1 = Counter(cadena_1)
    contador_2 = Counter(cadena_2)

    comunes = contador_1 & contador_2

    if len(comunes) == 0:
        return None
    
    comunes = list(comunes.elements())
    comunes = sorted(comunes)

    return comunes


texto_1 = 'Python'
texto_2 = 'PHP'
print(caracteres_comunes(texto_1, texto_2))

print()

texto_1 = 'JavaScript'
texto_2 = 'Java'
print(caracteres_comunes(texto_1, texto_2))

print()

texto_1 = 'Python'
texto_2 = 'C++'
print(caracteres_comunes(texto_1, texto_2))
