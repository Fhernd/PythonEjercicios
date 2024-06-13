# Ejercicio 1014: Usar una expresión lambda para ordenar una lista de cadenas a partir de su segundo carácter.

lenguajes = ['Python', 'JavaScript', 'C#', 'Go', 'PHP', 'Java']
print(lenguajes)

print()

# ['y', 'a', '#', 'o', 'H', 'a']
# ['#', 'H', 'a', 'a', 'o', 'y']
# => ['C#', 'PHP', 'JavaScript', 'Java', 'Go', 'Python']
resultado = sorted(lenguajes, key=lambda c: c[1])
print(resultado)
