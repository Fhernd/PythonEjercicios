# Ejercicio 604: Uso de la clase PriorityQueue para priorizar elementos de datos.

from queue import PriorityQueue

class Curso(object):
    def __init__(self, prioridad, nombre):
        self.prioridad = prioridad
        self.nombre = nombre
    
    def __lt__(self, otro):
        return self.prioridad < otro.prioridad

cursos = PriorityQueue()
cursos.put(Curso(3, 'Python'))
cursos.put(Curso(10, 'C++'))
cursos.put(Curso(1, 'Algoritmia'))

while not cursos.empty():
    c = cursos.get()
    print(c.prioridad, c.nombre)
