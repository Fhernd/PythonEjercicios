# Ejercicio 973: A partir de 4 dígitos dados en una lista generar la última hora en formato 24 horas.

from itertools import permutations

def ultima_hora(digitos):
    if not isinstance(digitos, list):
        raise TypeError('El argumento debe ser una lista.')
    
    if len(digitos) != 4:
        raise Exception('La lista debe contener cuatro elementos.')

    if not all([isinstance(e, int) for e in digitos]):
        raise TypeError('El argumento debe ser una lista con valores enteros.')
    
    if not all([d >= 0 for d in digitos]):
        raise Exception('Todos los elementos de la lista deben ser mayores o iguales 0.')

    digitos = [-d for d in digitos]

    digitos.sort()

    for h1, h2, m1, m2 in permutations(digitos):

        horas = -(10*h1 + h2)
        minutos = -(10*m1 + m2)

        if 60 > minutos >= 0 and 24 > horas >= 0:
            return '{:02}:{:02}'.format(horas, minutos)
    
    return None

print(ultima_hora([1, 3, 2, 7])) # 23:17
print(ultima_hora([5, 1, 2, 7])) # 17:51
