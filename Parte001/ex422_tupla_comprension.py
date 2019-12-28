# Ejercicio 422: Crear una tupla a partir de una tupla de comprensión.

cuadrados = tuple(n**2 for n in range(1, 11))

print(type(cuadrados))
print(len(cuadrados))
print(cuadrados)
