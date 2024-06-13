# Ejercicio 1007: Tomar los valores menores a 100 de una lista, y luego sumar a cada uno 10 unidades.

numeros = [150, 250, 183, 50, 10, 330, 25, 67]

menores_100 = filter(lambda n: n < 100, numeros)

resultado = list(map(lambda n: n + 10, menores_100))

print(resultado) # [60, 20, 35, 77]
