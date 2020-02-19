 # Ejercicio 644: Crear función para recorrido inorden de un árbol binario de búsqueda.

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

def inorden(raiz):
    if raiz is not None:
        inorden(raiz.izquierda)
        print(raiz.dato)
        inorden(raiz.derecha)


raiz = Nodo(21)
insertar(raiz, Nodo(13))
insertar(raiz, Nodo(10))
insertar(raiz, Nodo(33))
insertar(raiz, Nodo(18))
insertar(raiz, Nodo(25))
insertar(raiz, Nodo(40))

inorden(raiz)
