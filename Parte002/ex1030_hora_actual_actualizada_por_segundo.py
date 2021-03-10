# Ejercicio 1030: Usar el módulo time para mostrar la hora actual actualizada cada segundo.

import time

while True:
    hora_actual = time.strftime('%H:%M:%S')
    print(hora_actual)

    time.sleep(1)
