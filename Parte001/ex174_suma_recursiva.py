# Ejercicio 174: Calcular en n-ésimo término de una secuencia.

# Descripción del problema: Crear una secuencia donde los primeros cuatro números de la secuencia sean iguales a 1, y cada término sucesivo es igual a la suma de los primeros cuatro términos.

# n = 5 => (1, 2, 3, 4) => 1
# 1 + 1 + 1 + 1 = 4


def secuencia(n):
    if n == 1 or n == 2 or n == 3 or n == 4:
        return 1
    else:
        return secuencia(n - 1) + secuencia(n - 2) + secuencia(n - 3) + secuencia(n - 4)


print(secuencia(5))

# secuencia(4) + secuencia(3) + secuencia(2) + secuencia(1)
# 1 + 1 + 1 + 1 = 4

print(secuencia(6))

# secuencia(6):
# secuencia(5) + secuencia(4) + secuencia(3) + secuencia(2)

# secuencia(5):
# secuencia(4) + secuencia(3) + secuencia(2) + secuencia(1)
# 1 + 1 + 1 + 1 = 4

# 4 + 1 + 1 + 1 = 7
