# Ejercicio 640: Obtener un dato desde una lista doblemente enlazada a través de su índice.

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
    
    def eliminar(self, dato):
        actual = self.cabeza
        eliminado = False

        if actual is None:
            eliminado = False
        elif actual.dato == dato:
            self.cabeza = actual.siguiente
            self.cabeza.anterior = None
            eliminado = True
        elif self.cola.dato == dato:
            self.cola = self.cola.anterior
            self.cola.siguiente = None
            eliminado = True
        else:
            while actual:
                if actual.dato == dato:
                    # Antes: 2 = 3 = 5 = 7 = 11
                    # Actual: 3
                    # Después: 2 = 5 = 7 = 11
                    actual.anterior.siguiente = actual.siguiente
                    actual.siguiente.anterior = actual.anterior
                    eliminado = True
                actual = actual.siguiente
        
        if eliminado:
            self.contador -= 1
    
    def __getitem__(self, indice):
        if indice >= 0 and indice < self.contador:
            actual = self.cabeza

            for _ in range(indice - 1):
                actual = actual.siguiente
            
            return actual.dato
        else:
            raise Exception('Índice no válido. Está por fuera del rango.')

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

print()

print('Eliminación de datos:')
numero = 1
print('Cantidad de elementos antes de la eliminación:', numeros.contador)
numeros.eliminar(numero)
print('Cantidad de elementos después de la eliminación:', numeros.contador)
print('¿Este el valor 1 en la lista?:', numeros.buscar(numero))

print()

print('Acceso a un elemento por medio de su índice:')
# indice = -1
# print('Valor en la posición %i es igual a %i' % (indice, numeros[indice])) # Genera excepción
indice = 0
print('Valor en la posición %i es igual a %i' % (indice, numeros[indice]))
indice = 2
print('Valor en la posición %i es igual a %i' % (indice, numeros[indice]))
indice = 3
print('Valor en la posición %i es igual a %i' % (indice, numeros[indice]))
indice = 4
print('Valor en la posición %i es igual a %i' % (indice, numeros[indice]))
# indice = 7
# print('Valor en la posición %i es igual a %i' % (indice, numeros[indice])) # Genera excepción
