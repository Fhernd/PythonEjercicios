# Ejercicio 175: Reducir un número por medio de la suma de sus digitos.

# Descripción: Obtener un número entero positivo y sustraer la suma de sus digitos mientras que el número sea positivo.


def reducir_numero(n):
    cadena = str(n)
    contador = 0

    while n > 0:
        n -= sum([int(c) for c in cadena])
        cadena = str(n)

        contador += 1
    
    return contador


print(reducir_numero(7))
print(reducir_numero(29))

# n = 29
# cadena = '29', contador = 0
# n = 18
# cadena = '18', contador = 1
# n = 9
# cadena = '9', contador = 2
# n = 0
# cadena = '0', contador = 3
