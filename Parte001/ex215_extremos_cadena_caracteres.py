# Ejercicio 215: Extraer los n caracteres extremos de una cadena de caracteres.

# ¡Python es tremendo!
# ¡Po!
# ¡Podo!

def extraer_caracteres_extremos(cadena, n=1):
    if n * 2 <= len(cadena):
        return cadena[:n] + cadena[-n:]
    else:
        return ''


texto = '¡Python es tremendo!'

print(extraer_caracteres_extremos(texto))
print(extraer_caracteres_extremos(texto, 2))
print(extraer_caracteres_extremos(texto, 3))
print(extraer_caracteres_extremos(texto, 4))
print(extraer_caracteres_extremos(texto, 30))
