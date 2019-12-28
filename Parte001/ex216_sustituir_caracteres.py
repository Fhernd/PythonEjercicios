# Ejercicio 216: Sustituir por @ los caracteres que coincidan con el primer carácter excepto éste mismo.

# Solución:

# computición => computi@ión

# c, @omputa@ión

def sustituir_caracteres(cadena):
    primer_caracter = cadena[0]
    cadena = cadena.replace(primer_caracter, '@')

    return primer_caracter + cadena[1:]


texto = 'computición'
print(sustituir_caracteres(texto))

texto = 'elefante'
print(sustituir_caracteres(texto))
