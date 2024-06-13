# Ejercicio 1002: Extraer las vocales minúsculas desde un texto usando la función filter().

frase = 'Python Es Tremendo'
print(frase)

print()

vocales_minusculas = list(filter(lambda c: True if c in 'aeiou' else False, frase))
print(vocales_minusculas)
