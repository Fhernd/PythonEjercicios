# Ejercicio 845: Comprobar si una cadena contiene una lista de palabras.

import re

def contiene_palabras(palabras, frase):
    for p in palabras:
        if re.search(p, frase):
            print('La palabra `{}` se ha encontrado en la frase.'.format(p))
        else:
            print('La palabra `{}` NO se ha encontrado en la frase.'.format(p))


frase = 'Python es un lenguaje de programación multiparadigama. La versión actual es 3.8.2'
palabras = ['Python', 'versión', 'lenguaje', 'software', 'código']

contiene_palabras(palabras, frase)
