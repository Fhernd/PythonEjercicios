# Ejercicio 74: Crear una función para calcular la desviación estándar.

from math import sqrt


def desviacion_estandar(valores, media):
    suma = 0
    for valor in valores:
        suma += (valor - media) ** 2
    
    radicando = suma / (len(valores) - 1)

    return sqrt(radicando)


def calcular_media(valores):
    suma = 0
    
    for valor in valores:
        suma += valor
    
    return suma / len(valores)


if __name__ == "__main__":
    numeros = [7, 3, 13, 17, 10, 8, 12, 9]

    media = calcular_media(numeros)

    resultado = desviacion_estandar(numeros, media)

    print('La desviación estándar es: {}'.format(resultado))
