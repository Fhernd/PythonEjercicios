# Ejercicio 211: Invertir una cadena de caracteres.

def es_palindromo(frase):
    frase = frase.lower()
    frase = frase.replace(' ', '')
    
    return frase == frase[::-1]


print(es_palindromo('1001'))
print(es_palindromo('ataralarata'))
print(es_palindromo('Atar a la rata'))

print()

print(es_palindromo('1011'))
print(es_palindromo('python'))
