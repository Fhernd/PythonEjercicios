# Ejercicio 758: Redondear objeto Decimal al piso o al techo con la propiedad rounding.

import decimal

contexto = decimal.getcontext()
division = decimal.Decimal(1) / decimal.Decimal(17)
print('Valor actual de 1/17:', division)

contexto.prec = 4

print()

contexto.rounding = getattr(decimal, 'ROUND_FLOOR')
division = decimal.Decimal(1) / decimal.Decimal(17)
print('Valor actual de 1/17:', division)

print()

contexto.rounding = getattr(decimal, 'ROUND_CEILING')
division = decimal.Decimal(1) / decimal.Decimal(17)
print('Valor actual de 1/17:', division)
