# Ejercicio 944: Usar la función and_() de operator para la operación de conjunción lógica.

from operator import and_

# and

print(and_(5 > 3, 2 > 0)) # True
print(5 > 3 and 2 > 0) # True

print()

class Computador:
    def __init__(self, identificador, ram, ssd):
        self.id = identificador
        self.ram = ram
        self.ssd = ssd

computadores = []
computadores.append(Computador(1001, 8, 128))
computadores.append(Computador(1002, 16, 256))
computadores.append(Computador(1003, 8, 512))
computadores.append(Computador(1004, 32, 1024))

resultado = list(filter(lambda c: and_(c.ram >= 16, c.ssd >= 128), computadores))

for c in resultado:
    print(c.id, c.ram, c.ssd)
