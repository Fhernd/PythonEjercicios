# Ejercicio 742: Crear una función para obtener el n-ésimo número de Catalán.

def numero_catalan(n):
    if n <= 1:
        return 1
    
    resultado = 0

    for i in range(n):
        resultado += numero_catalan(i) * numero_catalan(n-i-1)
    
    return resultado


if __name__ == "__main__":
    for i in range(11):
        print(numero_catalan(i))
