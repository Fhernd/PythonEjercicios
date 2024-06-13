# Ejercicio 804: Encontrar los números cuadrados perfectos en un rango de valores.

def cuadrados_perfectos(a, b):
    cuadrados = []

    for i in range(a, b + 1):
        n = 1

        while n * n <= i:
            if n * n == i:
                cuadrados.append(i)
            
            n += 1
    
    return cuadrados

resultado = cuadrados_perfectos(1, 100)

print(resultado)
