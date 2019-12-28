# Ejercicio 23: Comprobar si un carácter dado es una vocal.

# c = 'i', ['a', 'e', 'i', 'o', 'u'] => True
# c = 'z', ['a', 'e', 'i', 'o', 'u'] => False


def es_vocal(c):
    """
    Comprueba si un carácter es una vocal
    """
    if len(c) == 1:
        vocales = 'aeiou'
        c = c.lower()

        return c in vocales
    else:
        return False


print(es_vocal('i'))
print(es_vocal('I'))
print(es_vocal('z'))
print(es_vocal('ae'))
