# Ejercicio 113: Validar si un número ingresado por el usuario es válido.

def es_numerico(cadena):
    try:
        int(cadena)
        return True
    except ValueError:
        return False


numero = input('Escriba un número entero: ')

if es_numerico(numero):
    print('Ha digitado un valor válido.')
else:
    print('El valor digitado no corresponde con un número.')
