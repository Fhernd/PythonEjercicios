# Ejercicio 794: Accesores para los atributos de una clase.

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f'({self.x}, {self.y})'


punto = Punto(2, 3)

print(punto)

print()

print('x: {p.x} - y: {p.y}'.format(p=punto))
