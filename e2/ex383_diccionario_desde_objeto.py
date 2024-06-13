# Ejercicio 383: Crear un diccionario a partir de los campos de un objeto.

class Color(object):
    def __init__(self, rojo, verde, azul):
        self.rojo = rojo
        self.verde = verde
        self.azul = azul


negro = Color(0, 0, 0)

print(negro)

negro_dict = negro.__dict__

print(type(negro_dict))
print(negro_dict)

azul = Color(0, 0, 255)

azul_dict = azul.__dict__

print(azul_dict)
