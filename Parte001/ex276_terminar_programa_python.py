# Ejercicio 276: Terminar la ejecución de un script Python con la función exit.

try:
    cadena = input('Digite un número: ')
    numero = int(cadena)
    exit(0)
except ValueError as e:
    print('Error:', e)
    exit(1)
