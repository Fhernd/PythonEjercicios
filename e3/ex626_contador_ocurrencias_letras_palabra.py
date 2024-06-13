# Ejercicio 626: Crear una función para contar las letras repetidas de una palabra.

# caballo -> a, l

from collections import Counter

def contar_letras_repetidas(texto):
    contador = Counter(texto)
    duplicados = [t[1] for t in list(contador.items()) if t[1] > 1]
    return len(duplicados)

texto = 'caballo'
print(contar_letras_repetidas(texto))
print(contar_letras_repetidas('serrucho'))
print(contar_letras_repetidas('programación'))
print(contar_letras_repetidas('Python'))
