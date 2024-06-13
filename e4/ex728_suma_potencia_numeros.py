# Ejercicio 728: Calcular la suma de los dígitos de la potencia de un número.

# 2^6 = 64 => 10

def suma_digitos_potencia(base, exponente):
    digitos_potencia = [int(d) for d in str(pow(base, exponente))]
    suma = sum(digitos_potencia)

    return suma

print(suma_digitos_potencia(2, 6))
print(suma_digitos_potencia(2, 100))
print(suma_digitos_potencia(3, 4))
