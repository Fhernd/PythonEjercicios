# Ejercicio 854: Extraer los números de una cadena de caracteres con la función re.split().

from re import split

frase = 'Cinco 5, Diez 10, Catorce 14, Veinte 20'

resultado = split('\D+', frase)

for n in resultado:
    print(n)
