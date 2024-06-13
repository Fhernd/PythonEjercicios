# Ejercicio 757: Cambiar la precisión de un objeto Decimal con la propiedad prec.

import decimal

division = decimal.Decimal(1/7)
print(division)
print(decimal.getcontext().prec)

for i in range(1, 11):
    decimal.getcontext().prec = i
    print('Precisión: {} - Valor: {}'.format(i, division * 1))
