# Ejercicio 635: Eliminar la primera ocurrencia de un dato desde una lista enlazada.

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
    
    def buscar(self, dato):
        for n in self.iterar():
            if dato == n:
                return True
        
        return False
    
    def __getitem__(self, indice):
        if indice >= 0 and indice < self.tamagnio:
            actual = self.cola

            for i in range(indice):
                actual = actual.siguiente
            
            return actual.dato
        else:
            raise Exception('Índice no válido. Está por fuera del rango.')
    
    def __setitem__(self, indice, nuevo_dato):
        if indice >= 0 and indice < self.tamagnio:
            actual = self.cola

            for i in range(indice):
                actual = actual.siguiente
            
            actual.dato = nuevo_dato
        else:
            raise Exception('Índice no válido. Está por fuera del rango.')
    
    def eliminar_dato(self, dato):
        actual = self.cola
        anterior = self.cola

        while actual:
            if actual.dato == dato:
                if actual == self.cola:
                    self.cola = actual.siguiente
                else:
                    # [2]->[3]->[5] => [2]->[5]
                    anterior.siguiente = actual.siguiente
                self.tamagnio -= 1
                return
            anterior = actual
            actual = actual.siguiente


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

print()

print('¿El número 11 existe en la lista enlazada numeros?:', numeros.buscar(11))
print('¿El número 3 existe en la lista enlazada numeros?:', numeros.buscar(3))

print()

primos = [2, 3, 5, 7]
print(primos[1])
print(primos[3])
print(primos[-1])

print()

# print(numeros[-1]) # Genera excepción
print(numeros[0])
print(numeros[3])
# print(numeros[4]) # Genera excepción

print()

# numeros[-1] = 1 # Genera excepción
print(numeros[3])
numeros[3] = 11
print(numeros[3])

# numeros[4] = 13 # Genera excepción

print()

# Eliminar la primera ocurrencia de una lista enlazada:
# 2 3 5 11
print('Cantidad de elementos antes de la inserción: ', numeros.tamagnio)
numeros.insertar(5)
print('Cantidad de elementos después de la inserción: ', numeros.tamagnio)
# 2 3 5 11 5

print()
numeros.eliminar_dato(5)
print('Después de la eliminación hay', numeros.tamagnio)
numeros.eliminar_dato(13)
print('Después de intentar eliminar el valor 11 hay', numeros.tamagnio, ' numeros')
numeros.eliminar_dato(11)
print('Cantidad de elementos después de la última eliminación:', numeros.tamagnio)
