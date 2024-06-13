# Ejercicio 1011: Ordenar con sorted() el resultado de juntar/fusionar dos listas con la función zip().

lenguajes = ['Python', 'Java', 'C#', 'JavaScript']
versiones = ['3.9.2', '15', '9', 'ES6']

# [('Python', '3.9.2'), ('Java', '15'), ...]

resultado = list(zip(lenguajes, versiones))
print(resultado)

print()

resultado = sorted(resultado)
print(resultado)

print()

resultado = sorted(resultado, reverse=True)
print(resultado)
