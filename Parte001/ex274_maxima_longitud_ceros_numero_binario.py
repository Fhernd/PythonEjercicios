# Ejercicio 274: Computar la cantidad máxima de ceros consecutivos en un número binario.

# Análisis:

# 1001100001 => 4
# 100010001000 => 3

def cantidad_maxima_ceros_consecutivos(binario):
    return max(map(len, binario.split('1')))


numero_binario = '1001100001'
print(numero_binario)
print(cantidad_maxima_ceros_consecutivos(numero_binario))

print()

numero_binario = '100010001000'
print(numero_binario)
print(cantidad_maxima_ceros_consecutivos(numero_binario))
