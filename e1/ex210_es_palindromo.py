# Ejercicio 210: Comprobar si una palabra o frase es palíndromo.

# Solución:

# oso, anita lava la tina, atar a la rata
# ataralarata
# izquierda = atara
# derecha = arata
# '1001'

def es_palindromo(frase):
    frase = frase.lower()
    frase = frase.replace(' ', '')
    longitud = len(frase)
    if longitud % 2 == 0:
        izquierda = frase[:longitud // 2]
        derecha = frase[longitud // 2:]
    else:
        izquierda = frase[:longitud // 2]
        derecha = frase[longitud // 2 + 1:]
    
    return izquierda == derecha[::-1]


print(es_palindromo('1001'))
print(es_palindromo('ataralarata'))

print()

print(es_palindromo('1011'))
print(es_palindromo('python'))
