# Ejercicio 235: Remover el carácter de nueva línea en una cadena de caracteres.

texto = 'Python es un lenguaje de programación\n'

print(texto, end='')

texto = texto.rstrip()

print(texto, end='')
