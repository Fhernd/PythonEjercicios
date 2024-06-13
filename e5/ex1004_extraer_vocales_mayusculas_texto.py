# Ejercicio 1004: Extraer las vocales mayúsculas desde un texto usando la función filter().

frase = 'Python Es Tremendo. Python Es Fácil De Aprender'Python Ejercicio: 1004 Extraer las Vocales Mayúsculas desde un Texto Usando la Función filter()
print(frase)

print()

vocales_mayusculas = list(filter(lambda c: c in 'AEIOU', frase))
print(vocales_mayusculas)
