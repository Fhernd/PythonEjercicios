# Ejercicio 533: Calcular el promedio de n cantidad de números enteros.

contador = 0
suma = 0
numero = 1

while numero != 0:
    numero = int(input('Digite un número entero (0 para terminar): '))
    
    if numero != 0:
        suma += numero
        contador += 1

if contador == 0:
    print('No digitó ningún número.')
else:
    promedio = suma / contador

    print('El promedio de los {} números es igual a {}.'.format(contador, promedio))
