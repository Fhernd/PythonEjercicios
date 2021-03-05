# Ejercicio 1009: Usar la función zip() para fusionar/juntar dos listas de elementos relacionados.

lenguajes = ['Python', 'Java', 'C#', 'JavaScript']
versiones = ['3.9.2', '15', '9', 'ES6']

# [('Python', '3.9.2'), ('Java', '15'), ...]

resultado = list(zip(lenguajes, versiones))
print(resultado)
