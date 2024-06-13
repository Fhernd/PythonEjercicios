# Ejercicio 1028: Calcular el promedio desde una lista indefinida de números enteros positivos.

suma = 0
contador = 0

while True:
    while True:
        try:
            numero = int(input('Ingrese un numero entero positivo (-1 para terminar): '))

            break
        except ValueError:
            print('MENSAJE: Debe digitar un número entero válido.')
        
        print()
    
    if numero <= 0:
        break
    
    suma += numero
    contador += 1

    print()

print()

if contador:
    promedio = suma / contador
    print(f'El promedio es igual a: {promedio}')
else:
    print('No digitó ningún valor entero positivo. No es posible calcular el promedio.')
