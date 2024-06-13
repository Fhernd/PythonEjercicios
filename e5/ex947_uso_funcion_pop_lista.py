# Ejercicio 947: Demostrar el uso básico de la función pop() de un objeto de tipo lista.

lenguajes = ['Python', 'JavaScript', 'Go', 'Java', 'C++']

print(lenguajes)
print(len(lenguajes))

print()

# pop([indice])

resultado = lenguajes.pop()
print(resultado)
print(lenguajes)
print(len(lenguajes))

print()

resultado = lenguajes.pop(2)
print(resultado)
print(lenguajes)
print(len(lenguajes))

print()

# resultado = lenguajes.pop(5) # IndexError
# 0, 1, 2, -1, -2, -3
