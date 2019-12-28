# Ejercicio 363: Comprobar si todos los elementos de una lista son mayores a un valor dado.

numeros_1 = [11, 13, 7, 5, 19]
numeros_2 = [11, 2, 13, 8, 5]
valor = 5

resultado = all(n >= valor for n in numeros_1)
print(resultado)

resultado = all(n >= valor for n in numeros_2)
print(resultado)
