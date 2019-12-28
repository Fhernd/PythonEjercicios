# Ejercicio 223: Remover los caracteres ubicados en índices impares dentro de un texto.

# Análisis:

# Python => Pto

def remover_caracteres_impares(cadena):
    resultado = ''

    for i in range(len(cadena)):
        if i % 2 == 0:
            resultado += cadena[i]
    
    return resultado


texto = 'Python'

print(remover_caracteres_impares(texto))
