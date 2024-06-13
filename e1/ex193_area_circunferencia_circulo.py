# Ejercicio 193: Calcular el área y la circunferencia de un círculo de radio r.

# Solución: 

# área = pi*r^2

# circunferencia = 2*pi*r

from math import pi

r = float(input('Escriba el valor del radio: '))

area = pi * r ** 2

print('El área del círculo es igual a {:.2f}'.format(area))

circunferencia = 2 * pi * r

print('La circunferencia del círculo es igual a {:.2f}'.format(circunferencia))
