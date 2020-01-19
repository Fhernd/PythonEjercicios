# Ejercicio 598: Crear una entidad tipo namedtuple para representar datos de un producto.

from collections import namedtuple

Producto = namedtuple('Producto', ['nombre', 'codigo', 'cantidad', 'precio'])
computador = Producto('Computador gamer', 'ABC123', 100, 967)

print(computador)
print(computador.codigo)
print(computador.nombre)
print(computador.cantidad)
print(computador.precio)
