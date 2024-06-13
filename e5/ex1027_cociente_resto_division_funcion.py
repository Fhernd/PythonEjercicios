# Ejercicio 1027: Definir una función para obtener el cociente y el resto de la división.

def cociente_resto_division(numerador, denominador):
    cociente = 0
    resto = 0

    while numerador >= denominador:
        numerador -= denominador
        resto = numerador
        cociente += 1
    
    return (cociente, resto)


resultado = cociente_resto_division(5, 2)
print(resultado)    # (2, 1)

print()

resultado = cociente_resto_division(9, 3)
print(resultado)    # (3, 0)

print()

resultado = cociente_resto_division(11, 4)
print(resultado)    # (2, 3)
