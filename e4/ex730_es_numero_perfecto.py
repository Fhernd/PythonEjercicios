# Ejercicio 730: Crear una función para determinar si un número es perfecto con lista de comprensión.

# 6 -> 1, 2, 3 => 1 + 2 + 3 = 6
# 28 -> 1 + 2 + 4 + 7 + 14 = 28

def es_numero_perfecto(numero):
    suma = sum([i for i in range(1, numero) if numero % i == 0])
    
    return suma == numero


print(es_numero_perfecto(6)) # 1 + 2 + 3 = 6
print(es_numero_perfecto(12)) # 1 + 2 + 3 + 4 + 6 = 16
print(es_numero_perfecto(28)) # 1 + 2 + 4 + 7 + 14 = 28
print(es_numero_perfecto(496))
print(es_numero_perfecto(8128))
