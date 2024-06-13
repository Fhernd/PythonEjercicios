# Ejercicio 786: Truncar y agregar padding a una cadena de caracteres con especificadores de formato.

frase = 'Python es tremendo'

print(frase)
print('{:.6}'.format(frase))
print('{:<10.6}'.format(frase))
print('{:<10.6}es un lenguaje de programación'.format(frase))
print('{:>10.6}'.format(frase))
print('{:_>10.6}'.format(frase))
print('{:_^10.6}'.format(frase))
