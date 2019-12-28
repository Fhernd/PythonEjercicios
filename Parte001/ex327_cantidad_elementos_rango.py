# Ejercicio 327: Crear función para computar la cantidad de elementos en un rango de valores.

def contar_elementos_rango(valores, limite_inferior, limite_superior):
    contador = 0

    for v in valores:
        if limite_inferior <= v <= limite_superior:
            contador += 1
    
    return contador


numeros = list(range(1, 11))

print(numeros)

resultado = contar_elementos_rango(numeros, 4, 7)
print(resultado)

print()

caracteres = ['a', 'b', 'c', 'c', 'c', 'd', 'e', 'f']
resultado = contar_elementos_rango(caracteres, 'b', 'd')
print(caracteres)
print(resultado)
