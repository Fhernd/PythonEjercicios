# Ejercicio 570: Crear una función lambda para convertir a mayúscula varias cadenas.

lenguajes = ['Python', 'JavaScript', 'Java', 'PHP', 'C++', 'Perl']
print(lenguajes)

print()

resultado = list(map(lambda c: c.upper(), lenguajes))
print(resultado)
