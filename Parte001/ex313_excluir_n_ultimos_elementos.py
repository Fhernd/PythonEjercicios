# Ejercicio 313: Excluir los n últimos números cuadrados para los valores 1 a 30.

def excluir_cuadrados(n):
    if n <= 30:
        cuadrados = [i**2 for i in range(1, 31)]

        return cuadrados[:-n]

    raise ValueError('n no debe ser mayor a 30')


print(excluir_cuadrados(5))
