# Ejercicio 770: Imprimir en pantalla la mantisa y el exponente de una lista de valores.

from math import ldexp

# b * (2^e)

print('{:^7}  {:^9}  {:^14}'.format('Mantisa', 'Exponente', 'Punto flotante'))
print('{:-^8} {:-^9}  {:-^14}'.format('', '', ''))

valores = [(0.5, 7), (0.3, -3), (0.9, 5), (0.2, -8)]

for m, e in valores:
    resultado = ldexp(m, e)

    print('{:7.2f} {:7d}     {:7.2f}'.format(m, e, resultado))
