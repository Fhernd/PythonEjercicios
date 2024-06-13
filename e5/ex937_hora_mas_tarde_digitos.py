# Ejercicio 937: Encontrar la hora más tarde a partir de 4 dígitos dados en una lista.

from itertools import permutations

def hora_mas_tarde(numeros):

    numeros = [n * -1 for n in numeros]
    
    numeros.sort()
    resultado = '00:00'

    for h1, h2, m1, m2 in permutations(numeros):
        horas = -(h1 * 10 + h2)
        minutos = -(m1 * 10 + m2)

        if 60 > minutos >= 0 and 24 > horas >= 0:
            resultado = '{:02}:{:02}'.format(horas, minutos)
            break
    
    return resultado

print(hora_mas_tarde([1, 2, 3, 4])) # 23:41

print()

print(hora_mas_tarde([8, 3, 9, 1])) # 19:38
