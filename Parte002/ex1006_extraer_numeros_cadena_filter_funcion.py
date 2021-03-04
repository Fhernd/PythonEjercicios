# Ejercicio 1006: Extraer los dígitos (números) que se hallan en un texto con la función filter().

frase = 'El año actual es 2021.'
print(frase)

print()

digitos = list(map(lambda d: int(d), list(filter(lambda c: c in '0123456789', frase))))
print(digitos)
