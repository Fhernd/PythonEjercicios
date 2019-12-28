# Ejercicio 167: Calcular el tercer lado de un triángulo rectángulo dados dos lados.

from math import sqrt


def pitagoras(cateto_adyacente, cateto_opuesto, hipotenusa):
    if cateto_adyacente == 'x':
        return 'cateto adyacente', sqrt(hipotenusa**2 - cateto_opuesto**2)
    elif cateto_opuesto == 'x':
        return 'cateto opuesto', sqrt(hipotenusa**2 - cateto_adyacente**2)
    elif hipotenusa == 'x':
        return 'hipotenusa', sqrt(cateto_adyacente**2 + cateto_opuesto**2)
    else:
        return None, None


print(pitagoras(5, 7, 'x'))
print(pitagoras('x', 5, 7))
print(pitagoras(5, 'x', 7))
print(pitagoras(5, 4.9, 7))
