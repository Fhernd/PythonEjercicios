# Ejercicio 709: Crear una clase personalizada para cálculos básicos sobre un triángulo.

class Triangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        resultado = self.base * self.altura / 2

        return resultado
    
    def perimetro(self, a, b, c):
        resultado = a + b + c

        return resultado


t = Triangulo(3, 5)
print('Área del triángulo: %.2f' % t.area())
print('Perimetro del triángulo: %.2f' % t.perimetro(2, 3, 7))
