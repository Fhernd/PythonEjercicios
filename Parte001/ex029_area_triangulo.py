# Ejercicio 29: Calcular el área de un triángulo.

base = None
altura = None

while True:
    try:
        base = float(input('Escriba la base del triángulo: '))
        break
    except:
        print('Debe escribir un número.')

while True:
    try:
        altura = float(input('Escriba la altura del triángulo: '))
        break
    except:
        print('Debe escribir un número.')


area = base * altura / 2

print('El área del triángulo es igual: {}'.format(area))
