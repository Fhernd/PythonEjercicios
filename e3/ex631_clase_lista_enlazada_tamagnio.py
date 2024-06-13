# Ejercicio 631: Escribir la lógica para contar los elementos de una lista enlazada.

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
        self.tamagnio += 1

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

print('Cantidad actual de elementos en la lista: %i' % numeros.tamagnio)

print()

for d in numeros.iterar():
    print(d)

print()

numeros.insertar(5)
numeros.insertar(7)

print('Cantidad actual de elementos en la lista: %i' % numeros.tamagnio)

print()

for d in numeros.iterar():
    print(d)
