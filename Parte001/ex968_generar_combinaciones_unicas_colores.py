# Ejercicio 968: Generar las combinaciones únicas a partir de un listado con diferentes colores.

from itertools import combinations

def combinacion_colores_unicos(colores, n):
    resultado = [' y '.join(c) for c in combinations(colores, r=n)]

    return resultado

datos = ['Rojo', 'Verde', 'Azul']
resultado = combinacion_colores_unicos(datos, 2)
print(resultado) # ['Rojo y Verde', 'Rojo y Azul', 'Verde y Azul']

print()

resultado = combinacion_colores_unicos(datos, 3)
print(resultado) # ['Rojo y Verde y Azul']
