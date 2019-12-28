# Ejercicio 271: Remover todos los caracteres duplicados de una cadena con fromKeys.

from collections import OrderedDict

def remover_caracteres_duplicados(frase):
    return ''.join(OrderedDict.fromkeys(frase))


texto = 'Python es un lenguaje de programación.'

print(texto)
print(remover_caracteres_duplicados(texto))
