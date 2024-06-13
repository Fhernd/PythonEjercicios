# Ejercicio 782: Diferencia entre las funciones incorporadas str() y repr().

# str(): para obtener la representación "informal" en cadena de caracteres de una variable o una literal.

# repr(): para obtener la representación "formal" en cadena de caracteres de una variable o una literal.

numero = 5

print(str(numero))

print(repr(numero))

print()

nombre = 'Edward'

print(str(nombre))

print(repr(nombre))

print()

nombre = "Edward"

print(str(nombre)) # Edward

print(repr(nombre)) # 'Edward'

print()

colores = {'Red': 13, 'Verde': 101, 'Azul': 203}

print(str(colores))

print(repr(colores))
