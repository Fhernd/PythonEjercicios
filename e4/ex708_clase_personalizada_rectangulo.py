# Ejercicio 708: Crear una clase personalizada para cálculos básicos sobre un rectángulo.

class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
    
    def area(self):
        resultado = self.ancho * self.alto

        return resultado
    
    def perimetro(self):
        resultado = 2 * (self.ancho + self.alto)

        return resultado


r = Rectangulo(10, 7)
print('Área del rectángulo: %.2f' % r.area())
print('Perímetro del rectángulo: %.2f' % r.perimetro())
