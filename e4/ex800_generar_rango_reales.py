# Ejercicio 800: Crear una función para generar un rango de valores reales (punto flotante).

def rango_valores_reales(inicio, final, salto=1.0):
    x = float(inicio)
    y = float(final)
    x_0 = x
    epsilon = salto / 2.0
    i = 0.0
    yield x

    while x + epsilon < y:
        i += 1.0
        x = x_0 + i * salto
        yield x


valores = list(rango_valores_reales(0.0, 1.0, 0.1))

print(valores)
print(len(valores))
