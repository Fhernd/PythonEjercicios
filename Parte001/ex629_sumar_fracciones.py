# Ejercicio 629: Crear una función para sumar fracciones y redondear al número entero más cercano.

def sumar_fracciones(fracciones):
    suma = 0

    for f in fracciones:
        suma += f[0]/f[1]
    
    return round(suma)


numeros = [(2, 3), (1, 2), (3, 2), (1, 3)]
resultado = sumar_fracciones(numeros)
print(resultado)
