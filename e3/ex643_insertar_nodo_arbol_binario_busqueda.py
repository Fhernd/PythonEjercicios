 # Ejercicio 643: Crear función para insertar un nodo en un árbol binario de búsqueda.

class Nodo:
    def __init__(self, dato):
        self.izquierda = None
        self.derecha = None
        self.dato = dato
 
def insertar(raiz, nodo):
    if raiz is None:
        raiz = nodo
    else:
        if raiz.dato < nodo.dato:
            if raiz.derecha is None:
                raiz.derecha = nodo
            else:
                insertar(raiz.derecha, nodo)
        else:
            if raiz.izquierda is None:
                raiz.izquierda = nodo
            else:
                insertar(raiz.izquierda, nodo)
