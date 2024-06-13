# Ejercicio 1031: Detener la ejecución del reloj creado en el ejercicio 1030.

import time

try:
    while True:
        hora_actual = time.strftime('%H:%M:%S')
        print(hora_actual)

        time.sleep(1)
except KeyboardInterrupt:
    print('El reloj se ha detenido.')
