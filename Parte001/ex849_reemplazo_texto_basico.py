# Ejercicio 849: Reemplazar espacio en blanco en una cadena con la función replace().

frase = '      Python        es  un lenguaje        de programación                 .'

print(frase)

frase = frase.strip()

print(frase)

print()

palabras = frase.split()

print(palabras)

print()

frase = ' '.join([p for p in palabras if p != '.']) + '.'

print(frase)
