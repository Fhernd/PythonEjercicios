# Ejercicio 734: Crear una función para generar una lista de los números de la suerte.

def numeros_suerte(n):
    numeros = list(range(-1, n**2 + 9, 2))
    
    i = 2

    while numeros[i:]:
        numeros = sorted(set(numeros) - set(numeros[numeros[i]::numeros[i]]))
        i += 1
    
    return numeros[1:n+1]

if __name__ == "__main__":
    resultado = numeros_suerte(5)

    print(resultado)
