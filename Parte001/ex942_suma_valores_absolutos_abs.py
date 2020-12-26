# Ejercicio 942: Calcular la suma del valor absoluto de varios números con la función abs() de operator.

import operator
from itertools import accumulate
# from operator import abs
# from operator import __abs__

numeros = [-3, 5, 7, 2, -11, 13]
print(numeros)

print()

numeros = list(map(operator.abs, numeros))
print(numeros)

print()

suma = list(accumulate(numeros, operator.add))
print(suma) # 41

print()

print(sum(numeros))
