# Ejercicio 953: Usar la función any() para validar si al menos un elemento de una colección es verdadero.

coleccion = [0, '', '123', True, (1, 2), ['John', 'Oliva', 'Juan'], {'a': 1}]
print(any(coleccion))  # True

print()

coleccion = ['', False, 0, not True, """""", '''''']
print(any(coleccion))  # False
