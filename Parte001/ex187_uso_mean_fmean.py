# Ejercicio 187: Uso de las funciones mean y fmean del módulo statistics.

from statistics import mean, fmean

numeros = [2, 3, 5, 7, 11, 13, 17, 19]

promedio = mean(numeros)

print(promedio)

numeros = [2.3, 5.5, 1.11, 17.19, 13.13]

promedio = fmean(numeros)

print(promedio)
