# Ejercicio 945: Calcular la división entera con la función floordiv() del módulo operator.

from operator import floordiv

# floordiv(a, b) ~= a // b ~= __floordiv__(a, b)

print(3 // 2)   # 1
print(floordiv(3, 2))   # 1

print()

numeros_1 = [2, 3, 5, 7, 11]
numeros_2 = [3, 2, 4, 8, 9]

for e in zip(numeros_1, numeros_2):
    print(floordiv(*e))
