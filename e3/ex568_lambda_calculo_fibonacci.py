# Ejercicio 568: Crear una función lambda para obtener valores de la serie Fibonacci.

from functools import reduce

generar_serie_fibonacci = lambda n: reduce(lambda a, _: a + [a[-1] + a[-2]], range(n-2), [0, 1])

valores = generar_serie_fibonacci(2)
print(valores)

valores = generar_serie_fibonacci(5)
print(valores)

valores = generar_serie_fibonacci(10)
print(valores)
