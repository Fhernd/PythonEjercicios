# Ejercicio 378: Calcular el producto de todos los valores de un diccionario.

def producto_valores(valores):
    producto = 1

    for v in valores:
        producto *= v

    return producto


numeros = {i: i**2 for i in range(1, 11)}

print(numeros)

valores = list(numeros.values())

print(valores)

resultado = producto_valores(valores)

print(resultado)
