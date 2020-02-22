# Ejercicio 657: Crear una función recursiva para calcular el máximo común divisor (MCD).

def mcd(a, b):
    minimo = min(a, b)
    maximo = max(a, b)

    if minimo == 0:
        return maximo
    elif minimo == 1:
        return 1
    else:
        return mcd(minimo, maximo % minimo)


print(mcd(4, 12)) # 4
print(mcd(6, 12)) # 6
print(mcd(3, 4)) # 3 => 1, 3, 4 => 1, 2, 4
