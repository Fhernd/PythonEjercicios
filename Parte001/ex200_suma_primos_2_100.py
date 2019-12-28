# Ejercicio 200: Suma de los números primos en el rango 2 a 100.

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


suma_primos = 0
generador_primos = generar_primo()

while True:
    primo = next(generador_primos)

    if primo <= 100:
        suma_primos += primo
    else:
        break

print('La suma de los números primos entre 2 y 100 es igual a {}.'.format(suma_primos))
