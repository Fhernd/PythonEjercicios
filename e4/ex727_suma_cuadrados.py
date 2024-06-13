# Ejercicio 727: Diferencia suma de los cuadrados y cuadrado de la suma de los primeros n números.

def diferencia(n=2):
    suma_cuadrados = 0
    suma = 0

    for n in range(1, n + 1):
        suma_cuadrados += n**2
        suma += n
    
    suma = suma ** 2

    return suma - suma_cuadrados


print(diferencia(5))
print(diferencia(10))
print(diferencia(20))
