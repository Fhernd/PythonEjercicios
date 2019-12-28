# Ejercicio 165: Calcular la suma de dos números sin usar el operador +.

# & 
# ^
# ~
# |
# <<
# >>


def suma_con_operador_bit(a, b):
    while b != 0:
        temp = a & b
        a = a ^ b
        b = temp << 1
    
    return a


# temp = 011 & 101 = 1
# a = 011 ^ 101 = 110
# b = 10

# temp = 110 & 010 = 010
# a = 110 ^ 010 = 100
# b = 0100

# temp = 0100 & 0100 = 0100
# a = 0100 ^ 0100 = 0000
# b = 01000

# temp = 00000 & 01000 = 00000
# a = 00000 ^ 01000 = 01000
# b = 000000

# a = 1000 = 8 [10]

print(suma_con_operador_bit(3, 5))
print(suma_con_operador_bit(10, 15))
