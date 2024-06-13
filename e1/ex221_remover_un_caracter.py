# Ejercicio 221: Remover el i-ésimo carácter de una cadena de caracteres.

# Python

def remover_i_esimo_caracter(palabra, i):
    izquierda = palabra[:i]
    derecha = palabra[i + 1:]

    return izquierda + derecha


texto = 'Python'
print(remover_i_esimo_caracter(texto, 2))
print(remover_i_esimo_caracter(texto, 3))
print(remover_i_esimo_caracter(texto, 4))
print(remover_i_esimo_caracter(texto, 5))
print(remover_i_esimo_caracter(texto, 10))
