# Ejercicio 993: Sucesión de valores de la forma 0, 1, 1, 2, 4, 7, 13, 24, ... según N términos.

# 0, 1, 1
# 0, 1, 1, 2
# 0, 1, 1, 2, 4, ...

def sucesion_valores(n):
    sucesion = [0, 1, 1]

    for i in range(n):
        sucesion.append(sum(sucesion[-3:]))

    return ','.join(str(e) for e in sucesion)

print(sucesion_valores(10)) # 0, 1, 1, 2, 4, 7, 13, 24, 44, 81, 149, 274, 504
