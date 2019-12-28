# Ejercicio 311: Generar los números cuadrados para los valores 1 a 30.

# Descripción: Generar los números cuadrados para los valores 1 a 30 y obtener los n primeros y n últimos cuadrados.

def generar_cuadrados(n):
    if 2 * n <= 30:
        cuadrados = [i ** 2 for i in range(1, 31)]

        return cuadrados[:n] + cuadrados[-n:]
    else:
        raise ValueError('n no debe ser mayor a 2*n')


resultado = generar_cuadrados(5)

print(resultado)
