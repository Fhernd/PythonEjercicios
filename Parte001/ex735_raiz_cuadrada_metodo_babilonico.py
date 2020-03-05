# Ejercicio 735: Calcular la raíz cuadrada de un número por el método babilónico.

from math import sqrt

def metodo_babilonico_raiz_cuadrada(n):
    if n < 0:
        raise ValueError('El valor de n no puede ser negativo')
    elif n == 0:
        return 0
    else:
        x = 2.0
        cociente = n / x
        promedio = (x + cociente) / 2.0

        while abs(cociente - promedio) > 0.00000000001:
            x = promedio
            cociente = n / x
            promedio = (x + cociente) / 2.0
        
        return promedio

numero = 2
print('Raíz cuadrada con la función sqrt:', sqrt(numero))
print('Raíz cuadrada con el método babilónico:', metodo_babilonico_raiz_cuadrada(numero))
