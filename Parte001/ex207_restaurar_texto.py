# Ejercicio 207: Restaurar un texto a partir de la versión acortada del texto.

# Descripción: Dado como texto acortado Python#4A3.8.0Tremend#3o, debería obtenerse PythonAAAA3.8.0Tremendooo


def restaurar_texto(acortado):
    resultado = ''
    indice = 0
    longitud = len(acortado)

    while indice < longitud:
        if acortado[indice] == '#':
            resultado += acortado[indice + 2] * int(acortado[indice + 1])
            indice += 3
        else:
            resultado += acortado[indice]
            indice += 1
    
    return resultado


texto_acortado = 'Python#4A3.8.0Tremend#3o'

print(restaurar_texto(texto_acortado))

print(restaurar_texto('Python 3.8.0'))
