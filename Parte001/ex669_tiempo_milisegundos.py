# Ejercicio 669: Obtener la cantidad de milisegundos transcurridos desde el inicio del tiempo Unix.

# Tiempo Unix: 1 enero, 1970

import time

segundos = time.time()
milisegundos = int(round(segundos * 1000))

print('Milisegundos desde el inicio del tiempo Unix: %i' % milisegundos)
