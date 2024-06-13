# Ejercicio 837: Verificar que exista una palabra donde la letra z no esté al inicio ni al final.

import re

def verificar_palabra(frase):
    patron = '\B(z|Z)\B'

    return bool(re.search(patron, frase))


texto = 'La zanahoria es de color naranja'
print(verificar_palabra(texto))

print()

texto = 'La zanahoria es una hortaliza'
print(verificar_palabra(texto))

print()

texto = 'LA ZANAHORIA ES UNA HORTALIZA'
print(verificar_palabra(texto))
