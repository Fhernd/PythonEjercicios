# Ejercicio 798: Parametrizar los especificadores de formato para valores numéricos.

nombre = 'Daniela'
ahorros = 1373.1719

print('Nombre:', nombre)
print('Ahorros:', ahorros)

print()

# Mecanismo tradicional (%) sin parametrizar:
print('Nombre: %s - Ahorros: %.2f' % (nombre[:4], ahorros))

# Mecanismo tradicional (%) sin parametrizar:
print('Nombre: %.4s - Ahorros: %.2f' % (nombre, ahorros))

cantidad_caracteres = 4
precision = 2

print('Nombre: %.*s - Ahorros: %.2f' % (cantidad_caracteres, nombre, ahorros))

print()

print('Nombre: {:.{c}} - Ahorros: {:.{p}f}'.format(nombre, ahorros, c=cantidad_caracteres, p=precision))
