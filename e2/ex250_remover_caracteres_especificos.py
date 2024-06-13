# Ejercicio 250: Remover un grupo de caracteres específicos de una cadena de caracteres.

# Solución:

# Python es tremendo => Pythn s trmnd

def remover_caracteres(cadena, caracteres):
    return ''.join(c for c in cadena if c not in caracteres)


texto = 'Python es tremendo'

print(remover_caracteres(texto, ['a', 'e', 'i', 'o', 'u']))
print(remover_caracteres(texto, 'aeiou'))
