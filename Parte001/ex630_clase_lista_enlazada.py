# Ejercicio 630: Crear una clase para representar una lista simplemente enlazada.

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.tamagnio = 0
    
    def insertar(self, dato):
        nodo = Nodo(dato)
        if self.cabeza:
            self.cabeza.siguiente = nodo
            self.cabeza = nodo
        else:
            self.cabeza = nodo
            self.cola = nodo
    
    def iterar(self):
        actual = self.cola

        while actual:
            dato = actual.dato
            actual = actual.siguiente
            yield dato


numeros = ListaEnlazada()
numeros.insertar(2)
numeros.insertar(3)

for d in numeros.iterar():
    print(d)

print()

numeros.insertar(5)
numeros.insertar(7)

for d in numeros.iterar():
    print(d)
