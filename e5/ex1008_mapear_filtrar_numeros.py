# Ejercicio 1008: Invertir el signo de los números de una lista, y luego tomar aquellos mayores a 100.

numeros = [-150, 50, 80, -1000, -20, 2, 3]

resultado = list(filter(lambda n: n > 100, map(lambda n: -n, numeros)))

# [150, -50, -80, 1000, 20, -2, -3]
# [150, 1000]

print(resultado)
