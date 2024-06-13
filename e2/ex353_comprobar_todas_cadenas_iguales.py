# Ejercicio 353: Comprobar si todas las cadenas de una lista son iguales a una cadena dada.

lenguajes = ['Python', 'Python', 'Python', 'Python']
cadena = 'Python'

resultado = all(c == cadena for c in lenguajes)

print(resultado)

print()

lenguajes.append('Java')

resultado = all(c == cadena for c in lenguajes)

print(resultado)
