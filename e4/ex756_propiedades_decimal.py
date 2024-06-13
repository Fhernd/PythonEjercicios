# Ejercicio 756: Obtener todas las propiedades públicas (contexto global) de los decimales.

import decimal

contexto = decimal.getcontext()

print('Exponencial máximo:', contexto.Emax)
print('Exponencial mínimo:', contexto.Emin)
print('Letra exponente e:', contexto.capitals)
print('Precisión:', contexto.prec)
print('Modo redondeo:', contexto.rounding)

print()

print('Banderas habilitadas:')
for k, v in contexto.flags.items():
    print('{}: {}'.format(k, v))

print()

print('Excepciones:')
for k, v in contexto.traps.items():
    print('{}: {}'.format(k, v))
