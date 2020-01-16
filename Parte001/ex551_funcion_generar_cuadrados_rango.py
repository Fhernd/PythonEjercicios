# Ejercicio 551: Crear función para generar números cuadrados para valores desde 1 hasta n.

def generar_cuadrados(n):
    cuadrados = []

    for i in range(1, n + 1):
        cuadrados.append(i**2)
    
    return cuadrados


resultado = generar_cuadrados(10)
print(resultado)
