# Ejercicio 330: Usar el método de Criba de Eratóstenes para generar números primos hasta n.

def criba_eratostenes(n):
    primos = []
    no_primos = []

    for i in range(2, n + 1):
        if i not in no_primos:
            primos.append(i)

            for j in range(i * i, n + 1, i):
                no_primos.append(j)
    
    return primos


print(criba_eratostenes(120))
print(len(criba_eratostenes(120)))
