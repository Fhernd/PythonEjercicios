# Ejercicio 980: Definir una función personalizada para calcular el producto cartesiano de dos listas.

def producto_cartesiano(datos):

    lista_1 = datos[0]
    lista_2 = datos[1]

    resultado = []

    for d in lista_1:

        for e in lista_2:
            resultado.append((d, e))
    
    return resultado

datos = [[1, 2], [3, 4]]

print(producto_cartesiano(datos)) # [(1, 3), (1, 4), (2, 3), (2, 4)]

print()

datos = [[1, 2, 3], [4, 5, 6]]
print(producto_cartesiano(datos)) # [(1, 4), (1, 5), (1, 6), (2, 4), (2, 5), (2, 6), (3, 4), (3, 5), (3, 6)]
