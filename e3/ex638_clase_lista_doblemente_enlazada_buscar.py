# Ejercicio 638: Crear método para buscar dato en una lista doblemente enlazada.

class Nodo(object):
    def __init__(self, dato=None, siguiente=None, anterior=None):
        self.dato = dato
        self.siguiente = siguiente
        self.anterior = anterior

class ListaDoblementeEnlazada(object):
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.contador = 0
    
    def insertar(self, dato):
        nodo = Nodo(dato)

        if self.cabeza is None:
            self.cabeza = nodo
            self.cola = self.cabeza
        else:
            nodo.anterior = self.cola
            self.cola.siguiente = nodo
            self.cola = nodo
        
        self.contador += 1
    
    def iterar(self):
        actual = self.cabeza

        while actual:
            dato = actual.dato
            actual = actual.siguiente
            yield dato

    def insertar_inicio(self, dato):
        if self.cabeza is not None:
            nodo = Nodo(dato)
            nodo.siguiente = self.cabeza
            self.cabeza.anterior = nodo
            self.cabeza = nodo

            self.contador += 1
    
    def buscar(self, dato):
        for d in self.iterar():
            if dato == d:
                return True
        
        return False

numeros = ListaDoblementeEnlazada()
print('Cantidad después de crear la lista:', numeros.contador)
numeros.insertar(2)
print('Cantidad después de insertar un elemento en la lista:', numeros.contador)

print()

numeros.insertar(3)
numeros.insertar(5)
numeros.insertar(7)
numeros.insertar(11)

print('Cantidad actual de elementos:', numeros.contador)

print()

for d in numeros.iterar():
    print(d)

print()

numeros.insertar_inicio(0)
numeros.insertar_inicio(1)
print('Cantidad de elementos después de insertar el valor cero:', numeros.contador)

for d in numeros.iterar():
    print(d)

print()

print('Búsqueda de un dato')
numero = 19
print('¿Se halla 19 en la lista?:', numeros.buscar(numero))
numero = 7
print('¿Se halla 7 en la lista?:', numeros.buscar(numero))
