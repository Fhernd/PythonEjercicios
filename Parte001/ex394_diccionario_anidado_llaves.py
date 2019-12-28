# Ejercicio 394: Convertir una lista de valores en un diccionario anidado de llaves.

numeros = [1, 2, 3, 4, 5]

nuevo_diccionario = {}
auxiliar = nuevo_diccionario

for n in numeros:
    nuevo_diccionario[n] = {}
    nuevo_diccionario = nuevo_diccionario[n]

print(auxiliar)
