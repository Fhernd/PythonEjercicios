# Ejercicio 238: Crear un algoritmo para implementar el cifrado César.

# Solución:

from string import ascii_lowercase, ascii_uppercase

def cifrado_cesar(texto, pasos):
    resultado = []

    for c in texto:
        if c in ascii_lowercase:
            indice = ascii_lowercase.index(c)
            nuevo_indice = (indice + pasos) % len(ascii_lowercase)
            resultado.append(ascii_lowercase[nuevo_indice])
        elif c in ascii_uppercase:
            indice = ascii_uppercase.index(c)
            nuevo_indice = (indice + pasos) % len(ascii_uppercase)
            resultado.append(ascii_uppercase[nuevo_indice])
        else:
            resultado.append(c)

    return ''.join(resultado)


texto = 'Python es tremendo'
print(cifrado_cesar(texto, 1))
print(cifrado_cesar(texto, 2))
print(cifrado_cesar(texto, 3))
