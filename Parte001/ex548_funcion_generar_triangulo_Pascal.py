# Ejercicio 548: Crear una función para generar n filas del triángulo de Pascal.

def triangulo_pascal(filas):
    fila = [1]
    cero = [0]

    for i in range(filas):
        print(fila)

        fila = [i + d for i, d in zip(fila + cero, cero + fila)]


triangulo_pascal(8)
