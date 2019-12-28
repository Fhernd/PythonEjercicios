# Ejercicio 110: Obtener los números divibles por 7 usando una función anónima.

numeros = [3, 14, 29, 42, 70, 2, 7, 8, 9, 13]

divisible_por_7 = lambda x: x % 7 == 0

numeros_div_7 = filter(divisible_por_7, numeros)

print(list(numeros_div_7))
