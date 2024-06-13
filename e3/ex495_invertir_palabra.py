# Ejercicio 495: Invertir una palabra escrita por el usuario utilizando un ciclo for.

def invertir_palabra(palabra):
    resultado = ''

    for c in range(len(palabra) - 1, -1, -1):
        resultado += palabra[c]
    
    return resultado


frase = input('Digite un palabra: ')

print(invertir_palabra(frase))
