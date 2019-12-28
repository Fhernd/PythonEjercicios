# Ejercicio 257: Alternar los separadores de millares y decimales con maketrans y translate.

valor = '12.345,67' # 12,345.67

print(valor)

cambio = valor.maketrans

valor = valor.translate(cambio('.,', ',.'))

print(valor)
