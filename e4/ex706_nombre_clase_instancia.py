# Ejercicio 706: Obtener el nombre de la clase de una instancia u objeto.

from datetime import datetime

class ClasePersonalizada:
    pass


cp = ClasePersonalizada()

print(type(cp).__name__)

ahora = datetime.now()

print(type(ahora))
print(type(ahora).__name__)
