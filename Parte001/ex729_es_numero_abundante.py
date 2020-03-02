# Ejercicio 729: Crear una función para determinar si un número dado es abundante.

# 12 => 1 + 2 + 3 + 4 + 6 => 16
# 13 => 1 => 1

def es_abundante(numero):
    factores = [f for f in range(1, numero) if numero % f == 0]
    suma = sum(factores)

    return suma > numero

print(es_abundante(12))
print(es_abundante(13))
