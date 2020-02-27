# Ejercicio 707: Crear una clase personalizada para cálculos básicos sobre un círculo.

from math import pi

class Circulo:
    def __init__(self, radio):
        self.radio = radio
    
    def area(self):
        resultado = pi * self.radio ** 2

        return resultado
    
    def perimetro(self):
        resultado = 2 * pi * self.radio

        return resultado


c = Circulo(5)

print('Área:', c.area())
print('Perímetro:', c.perimetro())
