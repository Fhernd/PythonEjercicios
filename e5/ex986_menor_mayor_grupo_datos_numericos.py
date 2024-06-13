# Ejercicio 986: Definir una función para encontrar el menor y el mayor entre un grupo de datos numéricos.

def encontrar_minimo_maximo(numeros):
    if not isinstance(numeros, (list, tuple)):
        raise TypeError('El argumento debe ser una lista o una tupla.')

    if len(numeros) == 0:
        return None
    
    minimo = numeros[0]
    maximo = numeros[0]

    for n in numeros:
        if n < minimo:
            minimo = n
        
        if n > maximo:
            maximo = n
    
    return minimo, maximo

primos = [13, 11, 2, 19, 5, 7, 23]

resultado = encontrar_minimo_maximo(primos)

print(resultado) # (2, 23)
