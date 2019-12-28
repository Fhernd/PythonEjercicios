# Ejercicio 6: Obtener un conjunto de números separados por coma y crear una lista.

# 2, 8, 9, 0, 1, 8

entrada = input('Escriba varios números separados por coma: ')

print(entrada)
print(type(entrada))

numeros = entrada.split(',')

print(type(numeros))
print(numeros)
