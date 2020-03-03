# Ejercicio 732: Crear una función para obtener la suma de los divisores de un número con lista de comprensión.

def suma_divisores(n):
    divisores = [i for i in range(1, n + 1) if n % i == 0]
    
    return sum(divisores)


resultado = suma_divisores(12) # 1 + 2 + 3 + 4 + 6 + 12 = 28
print(resultado)
resultado = suma_divisores(13) # 1 + 13 = 14
print(resultado)
resultado = suma_divisores(20) # 1 + 2 + 4 + 5 + 10 + 20 = 42
print(resultado)
resultado = suma_divisores(29) # 1 + 29 = 30
print(resultado)
