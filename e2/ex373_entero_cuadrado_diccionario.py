# Ejercicio 373: Crear un diccionario con valores cuadrados para cada i-ésima llave.

def valores_cuadrados(n):
    return {i: i**2 for i in range(1, n + 1)}


resultado = valores_cuadrados(5)

print(resultado)

print(valores_cuadrados(10))
