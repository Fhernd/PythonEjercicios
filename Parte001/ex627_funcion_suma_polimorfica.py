# Ejercicio 627: Crear una función para sumar o concatenar valores de manera polimórfica.

# 1 + 2 => 3
# '1' + '2' => '12'
# 1 + '2' => '12'

def suma_polimorfica(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a + b
    else:
        return '{}{}'.format(a, b)


print(suma_polimorfica(1, 2))
print(suma_polimorfica(1, '2'))
print(suma_polimorfica('1', '2'))
print(suma_polimorfica('1', 2))
