# Ejercicio 911: Usar la función accumulate() de itertools para acumular la multiplicación sucesiva de números.

# (1, 3, 5, 7) => 1, 3, 15, 105

from itertools import accumulate
import operator

def multiplicacion_sucesiva(numeros):
    return accumulate(numeros, operator.mul)

resultado = multiplicacion_sucesiva((1, 3, 5, 7))

for r in resultado:
    print(r, end=' ')

print()
print()

resultado = multiplicacion_sucesiva([1, 3, 5, 7])

for r in resultado:
    print(r, end=' ')
