# Ejercicio 954: Agrupar datos similares a través de la función groupby() del módulo itertools.

from itertools import groupby

monedas = ['bitcoin_1', 'billete_1', 'billete_2', 'moneda_10', 'moneda_1000', 'moneda_200', 'bitcoin_3', 'billete_3']
monedas.sort()

print(monedas)

print()

resultado = [list(datos) for _, datos in groupby(monedas, lambda e: e.split('_')[0])]
print(resultado)
