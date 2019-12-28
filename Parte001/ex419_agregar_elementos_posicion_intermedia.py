# Ejercicio 419: Agregar elementos en una posición intermedia de un objeto tupla.

def agregar_elementos(tupla, i, elementos):
    if 0 < i < len(tupla) - 1:
        return tupla[:i] + elementos + tupla[i:]

    return None


numeros = (1, 2, 6, 7)
i = 2
elementos = (3, 4, 5)

resultado = agregar_elementos(numeros, i, elementos)

print(resultado)
