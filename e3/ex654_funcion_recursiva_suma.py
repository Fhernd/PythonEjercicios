# Ejercicio 654: Crear función recursiva para sumar los valores n+(n-2)+(n-4) hasta n-x <= 0.

def sumar_valores(n):
    if n < 1:
        return 0
    else:
        return n + sumar_valores(n - 2)


print(sumar_valores(8))

# n = 8
# 8 + 12 = 20
#   n = 6
#   6 + 6
#       n = 4
#       4 + 2
#           n = 2
#           2 + 0
#               n = 0
