# Ejercicio 526: Crear una función para comprobar si una cadena representa un número.

def es_entero(cadena):
    return all(cadena[i] in '0123456789' for i in range(len(cadena)))


valor = input('Digite un número entero: ')

print(es_entero(valor))
