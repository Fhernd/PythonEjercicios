# Ejercicio 490: Encontrar los números divibles por 7 y múltiplos de 5 en un rango dado.

def numeros_divibles_multiplos(limite_inferior, limite_superior):
    if limite_superior > limite_inferior:

        resultado = []

        for n in range(limite_inferior, limite_superior + 1):
            if n % 7 == 0 and n % 5 == 0:
                resultado.append(n)
        
        return resultado

    raise ValueError('El límite inferior debe ser menor al límite superior.')


numeros = numeros_divibles_multiplos(500, 1000)

print(numeros)
