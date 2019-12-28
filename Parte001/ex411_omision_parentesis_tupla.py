# Ejercicio 411: Omitir los paréntesis al momento de crear un objeto de tipo tupla.

def fn():
    a = 1
    b = 2

    return a, b


tupla_1 = (1, 2, 3)
tupla_2 = 1, 2, 3

print(type(tupla_1))
print(type(tupla_2))
