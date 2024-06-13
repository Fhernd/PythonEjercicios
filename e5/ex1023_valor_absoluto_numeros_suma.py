# Ejercicio 1023: Calcular el valor absoluto de un conjunto de números y luego calcular su suma.

numeros = [10, -100, -50, 5, -100, -5, 200, -200]
print(numeros)

print()

numeros_absolutos = list(map(lambda n: abs(n), numeros))
print(numeros_absolutos)

print()

suma = sum(numeros_absolutos)
print(suma) # 670
