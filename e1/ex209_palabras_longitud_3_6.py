# Ejercicio 209: Obtener sólo las palabras de longitud de 3 a 6 caracteres.

# Solución:

# Python es génial => Python génial
# Esa canción suena muy bien => Esa canción suena muy bien


def extraer_palabras(frase):
    frase = frase.replace(',', '')
    frase = frase.replace('.', '')

    palabras = [p for p in frase.split() if 3 <= len(p) <= 6]

    return palabras


texto = 'Python es génial.'
print(extraer_palabras(texto))

texto = 'Esa canción suena muy bien'
print(extraer_palabras(texto))
