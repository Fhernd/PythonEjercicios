# Ejercicio 864: Remover el espacio intermedio que halla entre cada palabra de una frase.

from re import sub

texto = 'Python            es un                  lenguaje de            programación    multiparadigma.'

print(len(texto))
print(texto)

print()

patron = ' +'

resultado = sub(patron, ' ', texto)

print(len(resultado))
print(resultado)
