# Ejercicio 710: Crear una jerarquía de herencia para figuras geométricas: círculo y rectángulo.

from abc import ABC, abstractmethod
from math import pi

class Figura(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimetro(self):
        pass

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio
    
    def area(self):
        resultado = pi * self.radio ** 2

        return resultado
    
    def perimetro(self):
        resultado = 2 * pi * self.radio

        return resultado

class Rectangulo(Figura):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
    
    def area(self):
        resultado = self.ancho * self.alto

        return resultado
    
    def perimetro(self):
        resultado = 2 * (self.ancho + self.alto)

        return resultado

c = Circulo(5)

print('Cálculos del círculo:')
print('Área:', c.area())
print('Perímetro:', c.perimetro())

print()


r = Rectangulo(10, 7)
print('Cálculos del rectángulo:')
print('Área del rectángulo: %.2f' % r.area())
print('Perímetro del rectángulo: %.2f' % r.perimetro())
