# Ejercicio 1035: Definir una jerarquía de herencia a partir de la clase Thread para crear un reloj.

import datetime
import threading
import sys
import time

class Reloj(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
    
    def run(self):
        while True:
            tiempo_transcurrido = time.time()
            fecha = datetime.datetime.fromtimestamp(tiempo_transcurrido)
            hora_formateada = fecha.strftime('%H:%M:%S')
            print(hora_formateada)

            sys.stdout.flush()

            time.sleep(1)


reloj = Reloj()
reloj.start()
