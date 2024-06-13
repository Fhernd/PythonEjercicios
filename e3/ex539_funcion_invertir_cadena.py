# Ejercicio 539: Crear una función personalizada para invertir una cadena de caracteres.

def invertir_cadena(texto):
    resultado = ''
    indice = len(texto)

    while indice > 0:
        resultado += texto[indice - 1]
        indice -= 1
    
    return resultado


lenguaje = 'nohtyP'
print(invertir_cadena(lenguaje))

print(invertir_cadena('Python'))
