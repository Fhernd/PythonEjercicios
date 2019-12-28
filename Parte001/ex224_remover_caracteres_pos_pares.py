# Ejercicio 224: Remover los caracteres ubicados en índices pares dentro de un texto.

# Análisis:

# Python -> yhn

def remover_caracteres_pares(palabra):
    resultado = []

    for i in range(len(palabra)):
        if i % 2 == 1:
            resultado.append(palabra[i])
    
    return ''.join(resultado)


texto = 'Python'
print(remover_caracteres_pares(texto))
