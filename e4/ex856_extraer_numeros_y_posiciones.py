# Ejercicio 856: Extraer los números y posiciones desde una cadena de caracteres.

import re

frase = 'En el canal de YouTube hay aproximadamente 653 vídeos de Ejercicios de JavaScript. También se encuentra alrededor de 400 Ejercicios de Java. De manera análoga para el lenguaje de programación Python se pueden encontrar alrededor de 850 vídeos actualmente. En cuanto a Lodash, hay 10 ejercicios.'

patron = '\d+'

for r in re.finditer(patron, frase):
    print('Número:', r.group(0))
    print('Posición:', r.start())
    print()
