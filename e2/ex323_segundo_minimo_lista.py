# Ejercicio 323: Encontrar el segundo número más pequeño en una lista.

def segundo_menor(numeros):
    if isinstance(numeros, list):
        if len(numeros) < 2:
            return None

        if len(numeros) == 2 and numeros[0] == numeros[1]:
            return numeros[0]

        duplicados = set()
        unicos = []

        for n in numeros:
            if n not in duplicados:
                duplicados.add(n)
                unicos.append(n)
        
        unicos.sort()
        
        return unicos[1]

    raise TypeError('El parámetro numeros debe ser una lista')


numeros = [1, 3, 3, 7, 9, 11, 13, -5, 0, -1, 8, 12, 16, -5, -5]

print(segundo_menor(numeros))
