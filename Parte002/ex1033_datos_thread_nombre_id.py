# Ejercicio 1033: Obtener el nombre y el identificador de un thread mientras éste se ejecuta.

import threading
import os

def visualizar_datos_tarea_1():
    print(f'Nombre del thread t1: {threading.current_thread().name}')
    print(f'ID del thread t1: {os.getpid()}')


def visualizar_datos_tarea_2():
    print(f'Nombre del thread t2: {threading.current_thread().name}')
    print(f'ID del thread t2: {os.getpid()}')


if __name__ == '__main__':
    print(f'ID del proceso principal (main): {os.getpid()}')
    print(f'Nombre del proceso principal (main): {threading.current_thread().name}')

    t1 = threading.Thread(target=visualizar_datos_tarea_1, name='Thread No. 1')
    t2 = threading.Thread(target=visualizar_datos_tarea_2, name='Thread No. 2')

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print('El proceso principal ha terminado.')
