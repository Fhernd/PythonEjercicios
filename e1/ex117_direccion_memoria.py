# Ejercicio 117: Validar que dos cadenas caracteres tienen la misma ubicación en memoria.

lenguaje = 'Python'

frase = 'Python es tremendo!'

print(hex(id(lenguaje)))
print(hex(id(frase)))

lenguaje = lenguaje + ' 3.8.0'

print(hex(id(lenguaje)))

cadena = 'Python'

print(hex(id(cadena)))
