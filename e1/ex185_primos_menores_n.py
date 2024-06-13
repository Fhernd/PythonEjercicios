# Ejercicio 185: Encontrar todos los números primos menores a un número n dado.

# Función creada en el ejercicio 90:
def generar_primo():
    numero = 2

    yield numero

    while True:
        temp = numero
        while True:
            temp += 1
            contador = 1
            contador_divisores = 0

            while contador <= temp:
                if temp % contador == 0:
                    contador_divisores += 1 
                
                if contador_divisores > 2:
                    break
                
                contador += 1
            
            if contador_divisores == 2:
                yield temp


def primos_menores(n):
    generador = generar_primo()
    primos = []

    while True:
        primo = next(generador)
        if primo < n:
            primos.append(primo)
        else:
            break

    return primos


print(primos_menores(15))
