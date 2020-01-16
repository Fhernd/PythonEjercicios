# Ejercicio 541: Crear una función para comprobar si un número dado se halla en un rango.

def esta_en_rango(rango, numero):
    return numero in range(*rango)

print(esta_en_rango([1, 6], 2))
print(esta_en_rango([1, 6], -1))
print(esta_en_rango([1, 6], 6))
print(esta_en_rango([1, 6], 5))
