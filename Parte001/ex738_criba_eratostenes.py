# Ejercicio 738: Crear una función para generar números primos a partir de la criba de Eratóstenes.

def criba_eratostenes(n):
    primos = []
    no_primos = set()

    for i in range(2, n + 1):
        if i in no_primos:
            continue
        
        for j in range(i*2, n + 1, i):
            no_primos.add(j)
        
        primos.append(i)
    
    return primos

if __name__ == "__main__":
    resultado = criba_eratostenes(120)
    print(len(resultado))
    print(resultado)
