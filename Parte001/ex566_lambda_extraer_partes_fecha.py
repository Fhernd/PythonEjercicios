# Ejercicio 566: Crear una función lambda para extraer las partes de un objeto fecha.

from datetime import datetime

ahora = datetime.now()
print(ahora)

print()

extrear_partes_fecha = lambda f: (f.year, f.month, f.day, f.time())
resultado = extrear_partes_fecha(ahora)
print(resultado)
