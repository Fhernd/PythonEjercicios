# Ejercicio 713: Encontrar todos los subconjuntos únicos posibles de una lista.

def subconjuntos(numeros):
    return subconjuntos_recursivo([], sorted(numeros))

def subconjuntos_recursivo(actual, conjunto):
    if conjunto:
        return subconjuntos_recursivo(actual, conjunto[1:]) + subconjuntos_recursivo(actual + [conjunto[0]], conjunto[1:])
    return [actual]


numeros = [1, 2, 3, 4, 5]
resultado = subconjuntos(numeros)

print(len(resultado)) # 2^n => 2^5 = 32
print(resultado)
