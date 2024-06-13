# Ejercicio 312: Excluir los n primeros números cuadrados para los valores 1 a 30.

def excluir_cuadrados(n):
    if n <= 30:
        cuadrados = [i**2 for i in range(1, 31)]

        return cuadrados[n:]

    raise ValueError('n no puede ser mayor a 30')


print(excluir_cuadrados(5))
