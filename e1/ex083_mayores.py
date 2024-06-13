# Ejercicio 83: Comprobar que todos los elementos de una colección son mayores respecto a un número.

numeros = [7, 3, 2, 5, 11]

print(all(x > 1 for x in numeros))
print(all(x > 5 for x in numeros))
