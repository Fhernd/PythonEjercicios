# Ejercicio 251: Obtener los caracteres que se repiten en una cadena.

# Solución:

from collections import defaultdict

texto = 'Python es un lenguaje de programación'

contador = defaultdict(int)

for c in texto:
    contador[c] += 1

for c in sorted(contador, key=contador.get, reverse=True):
    if contador[c] > 1:
        print('El carácter %s se repetir %i' % (c, contador[c]))
