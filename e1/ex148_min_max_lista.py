# Ejercicio 148: Encontrar el mínimo y el máximo de una lista sin usar funciones existentes.

# min, max


def min_max(numeros):
    """
    Encuentra el menor y el mayor de una lista de números.
    """
    if len(numeros) > 0:
        menor = numeros[0]
        mayor = numeros[0]

        for n in numeros:
            if n < menor:
                menor = n
            
            if n > mayor:
                mayor = n
        
        return menor, mayor
    else:
        return None


datos = [9, 3, 2, 13, 0, 23, 8, 7]

print(min_max(datos))

datos = []

print(min_max(datos))
