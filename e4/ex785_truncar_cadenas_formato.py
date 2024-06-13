# Ejercicio 785: Truncar una cadena de caracteres con especificadores de formato.

frase = '¡Python es tremendo!'

print(frase)
print('%s' % frase)
print('{0}'.format(frase))

print()

subcadena = frase[:7]

print(subcadena)

print()

# Mecanismo tradicional:
print('%.7s' % frase)

# Nuevo mecanismo:
print('{:.7}'.format(frase))
