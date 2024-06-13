# Ejercicio 943: Calcular la suma del precio de varios productos con la función add() de operator.

from operator import add
from itertools import accumulate

class Producto:

    def __init__(self, identificador, nombre, precio):

        self.identificador = identificador
        self.nombre = nombre
        self.precio = precio

productos = []
productos.append(Producto(1001, 'Smartphone', 500))
productos.append(Producto(1002, 'Teclado gamer', 200))
productos.append(Producto(1003, 'Mouse gamer', 120))
productos.append(Producto(1004, 'Monitor 32"', 300))

suma = list(accumulate(list(map(lambda p: p.precio, productos)), add))[-1]

print(suma) # 1120
