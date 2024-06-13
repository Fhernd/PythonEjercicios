# Ejercicio 282: Crear función para encontrar la palabra más corta en una frase.

def palabra_mas_corta(frase):
    palabras = frase.split()

    mas_corta = palabras[0]

    for i in range(1, len(palabras)):
        if len(mas_corta) > len(palabras[i]):
            mas_corta = palabras[i]
    
    return mas_corta


frase = 'Python es un lenguaje de programación'
print(palabra_mas_corta(frase))

frase = "Python PHP C# JavaScript Java"
print(palabra_mas_corta(frase))
