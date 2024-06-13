# Ejercicio 653: Crear una función recursiva para sumar los dígitos de un número entero.

# 253 => 2, 5, 3 => 2 + 5 + 3 = 10

def sumar_digitos(numero):
    if numero == 0:
        return 0
    else:
        return numero % 10 + sumar_digitos(numero // 10)

print(sumar_digitos(253)) # 10
print(sumar_digitos(123)) # 6
print(sumar_digitos(12345)) # 15
