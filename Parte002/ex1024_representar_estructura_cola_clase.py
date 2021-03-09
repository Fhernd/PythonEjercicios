# Ejercicio 1024: Crear una clase para representar la estructura de datos cola (queue) usando una lista.

# FIFO: First-In-First-Out ~= Primero en entrar, primero en salir

class Cola:

    def __init__(self):
        self.datos = []
    
    def cantidad(self):
        return len(self.datos)
    
    def insertar(self, dato):
        self.datos.insert(0, dato)
    
    def extraer(self):
        if self.cantidad():
            return self.datos.pop()
        else:
            return None
    
    def primer_dato(self):
        if self.cantidad():
            return self.datos[-1]
    
    def ultimo_dato(self):
        if self.cantidad():
            return self.datos[0]

numeros = Cola()
numeros.insertar(2)
numeros.insertar(3)
numeros.insertar(5)
numeros.insertar(7)

print(numeros.primer_dato())    # 2
print(numeros.ultimo_dato())    # 7
print(numeros.cantidad())   # 4

print()

dato = numeros.extraer()
print(dato) # 2
print(numeros.cantidad()) # 3

print()

numeros.extraer()
numeros.extraer()
numeros.extraer()
print(numeros.cantidad()) # 0

print()

dato = numeros.extraer()
print(dato) # None
