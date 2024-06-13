# Ejercicio 283: Crear función para encontrar la palabra más larga en una frase.

def palabra_mas_larga(frase):
    palabras = frase.split()

    mas_larga = palabras[0]

    for i in range(1, len(palabras)):
        if len(mas_larga) < len(palabras[i]):
            mas_larga = palabras[i]
    
    return mas_larga


frase = 'Python es un lenguaje de programación'
print(palabra_mas_larga(frase))

frase = 'Python JavaScript C# Java PHP'
print(palabra_mas_larga(frase))
