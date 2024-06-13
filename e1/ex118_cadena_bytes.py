# Ejercicio 118: Crear la representación en cadena de bytes desde una cadena de caracteres.

frase = 'Python es tremendo!'

print(frase)
print(type(frase))

cadena_bytes = bytes(frase, 'utf-8')

print(cadena_bytes)
print(type(cadena_bytes))
