# Ejercicio 525: Calcular la suma de 2 números. Si la suma está entre 15 y 30, retornar 20.

def calcular_suma(a, b):
    suma = a + b

    if suma in range(15, 31):
        return 20
    
    return suma


operando_1 = 13
operando_2 = 30
print(calcular_suma(operando_1, operando_2))

operando_1 = 13
operando_2 = 15
print(calcular_suma(operando_1, operando_2))
