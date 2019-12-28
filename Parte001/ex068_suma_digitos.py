# Ejercicio 68: Sumar los dígitos de un número entero positivo.

# 1234 => 1 + 2 + 3 + 4 = 10

numero = input('Escriba un número entero positivo: ')

lista_digitos = list(numero)

print(lista_digitos)

lista_digitos = [int(c) for c in lista_digitos]

print(lista_digitos)

suma = sum(lista_digitos)

print(suma)

suma = sum([int(c) for c in numero])

print(suma)
