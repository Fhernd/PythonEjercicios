# Ejercicio 661: Obtener la hora actual por medio de la función time() de la clase datetime.

from datetime import datetime

hora = datetime.now().time()

print(hora)
print(type(hora))
