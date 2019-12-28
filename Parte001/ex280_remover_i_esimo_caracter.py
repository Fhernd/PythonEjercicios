# Ejercicio 280: Crear una función básica para remover el i-ésimo carácter de una cadena.

def remover_caracter(cadena, i):
    resultado = ''

    for j in range(len(cadena)):
        if j != i:
            resultado += cadena[j]
    
    return resultado


frase = 'Python es tremendo!'
posicion = 3

print(remover_caracter(frase, posicion))
