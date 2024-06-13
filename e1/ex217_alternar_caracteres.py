# Ejercicio 217: Alternar el segundo carácter entre dos palabras de tres letras.

# Solución:

# las los => los las

def intercambiar_caracteres(palabra1, palabra2):
    if len(palabra1) == 3 and len(palabra2) == 3:
        nueva_palabra1 = palabra1[0] + palabra2[1] + palabra1[2]
        nueva_palabra2 = palabra2[0] + palabra1[1] + palabra2[2]

        return nueva_palabra1, nueva_palabra2
    else:
        raise ValueError('Las palabras no son de 3 caracteres.')


print(('las', 'los'))
print(intercambiar_caracteres('las', 'los'))
