# Ejercicio 503: Capturar binarios de 4 bits separados por coma y validar si son divibles por 5.

numeros = []

cadena = input('Escriba números binarios de 4 bits separados por coma: ')

binarios = [b for b in cadena.split(',')]

for b in binarios:
    entero = int(b, 2)

    if not entero % 5:
        numeros.append(b)

print(', '.join(numeros))
